#include <opencv2/opencv.hpp>
#include <iostream>
#include <opencv2/imgproc.hpp>
#include <opencv2/video.hpp>
#include "opencv2/highgui.hpp"
#include <vector>
#include <opencv2/imgcodecs.hpp>
#include <string>
#include <fstream>
#include <chrono>
#include <pthread.h>

using namespace cv;
using namespace std;
using namespace std::chrono;

vector<Point2f> pts_src;
int n=0;
Mat im_src, h;
vector<Point2f> pts_dst;
Rect box;

// struct for passing parameter to thread function
struct frames{
    Mat base;
    Mat current;
};



void write_csv(string filename, vector<double> queueDensity, vector<double> dynamicDensity){
    // if(queueDensity.size()!=dynamicDensity.size()){
    //     cout << "Incompatible vectors" << endl;
    //     return ;
    // }
    int k = queueDensity.size();
    ofstream myFile(filename);
    // "framenum, queue density, dynamic density"
    myFile << "#framenum" << "," <<  "queue density" << "\n";
    for(int i = 0; i< k; i ++){
        myFile << i+1 << "," << queueDensity[i] << "\n";
    }
    myFile.close();
}

void mouseFun(int event, int x, int y, int flag, void* userdata){
    if(event==EVENT_LBUTTONDOWN){
        //cout<< x<<" "<<y << endl;
        pts_src.push_back(Point2f(x,y));
        n++;

        if(n>=4){
            imshow("photo",im_src);
            destroyAllWindows();
        }
    }    
}

double q_density(Mat input, Mat empty_road){
    Mat image_diff, thresh;
    vector<vector<Point>> conts;

    //store the diff of the image in imag_diff
    absdiff(input, empty_road, image_diff);
    threshold(image_diff, thresh, 45, 255, 0);

    findContours(thresh, conts, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

    int net_area = empty_road.cols;
    net_area = net_area*empty_road.rows;

    int covered_area = 0;

    vector< vector<Point> > hull(conts.size());

    for(int i = 0; i < conts.size(); i++){
        convexHull(Mat(conts[i]), hull[i], false);
    }   

    for(int i = 0; i < conts.size(); i++){
        covered_area = covered_area + contourArea(conts[i], 0);
    }

    double ret = (double)covered_area;
    ret = ret/((double)net_area);

    return ret;
}

Mat angleCorrectionAndCrop(Mat img){
    Mat angle_corrected;
    warpPerspective(img, angle_corrected, h, img.size());
    Mat crop(angle_corrected, box);

    return crop; 
} 

void* fun(void* args){
    frames* f = (frames*) args;
    frames f1 = *f;
    //cout << "size of f->current in fun1: "<<f1.current.rows<<"/"<<f1.current.cols<<endl;
    //cout << "size of f->base in fun1: "<<f1.base.rows<<"/"<<f1.base.cols<<endl;
    double* density = new double(0);
    *density = q_density(f1.current,f1.base);
    //cout << "output from fun1 "<<*density<<endl;
    return density;   
}

int main(int argc, char* argv[])
{      
    //take number of threads as command line input
    int num = stoi(argv[1]); 

    pts_src.push_back(Point2f(973,223));

    pts_src.push_back(Point2f(477,1066));

    pts_src.push_back(Point2f(1558, 1069));

    pts_src.push_back(Point2f(1275, 230));



    pts_dst.push_back(Point2f(472,52));

    pts_dst.push_back(Point2f(472,830));

    pts_dst.push_back(Point2f(800, 830));

    pts_dst.push_back(Point2f(800, 52));

    h = findHomography(pts_src, pts_dst);

    int x_min,x_max,y_min,y_max;
   

    x_min=x_max=pts_dst[0].x;
    y_min=y_max=pts_dst[0].y;

    for(int i=1;i<4;i++){
        if(x_min>pts_dst[i].x)x_min=pts_dst[i].x;
        if(y_min>pts_dst[i].y)y_min=pts_dst[i].y;
        if(x_max<pts_dst[i].x)x_max=pts_dst[i].x;
        if(y_max<pts_dst[i].y)y_max=pts_dst[i].y;
    }

    box.x=x_min;
    box.y=y_min;
    box.width=x_max-x_min;
    box.height=y_max-y_min;

    //------------------------------------------------------------------------------------------
    auto start = high_resolution_clock::now();

    pthread_t t[num];
    //1, t2, t3, t4;
    double d1,d2,d3,d4;
    void* density[num];
    for(int i=0; i<num; i++){
        density[i]=NULL;
    }
    
    Mat empty;
    empty = imread("empty.jpg", IMREAD_GRAYSCALE);
    empty = angleCorrectionAndCrop(empty);

    //imshow("cropped empty road",empty);
    //waitKey(0);

    VideoCapture cap("trafficvideo.mp4");
    if(!cap.isOpened()){
        cout << "Error opening video stream or file" << endl;
        return -1;
    }

    int count = 0;

    Mat prev;

    vector<double> dynamic_density;
    dynamic_density.push_back(0.1);
    vector<double> queueDensity;    
    vector<int> correspoding_frame;

    int i=0;
    double* temp;
    Mat frame,grayscale;
    frames f[num];

    /// handle the last few frames later
    while(true){
        
        // Capture frame-by-frame
        cap>>frame;

        // If the frame is empty, break immediately
        if (frame.empty())
            break;         

        // processing every 5th frame
        if(count%5 == 0){

            //convert current frame into grayscale, then do angle correction and cropping
            cvtColor(frame, grayscale, COLOR_BGR2GRAY);
            grayscale = angleCorrectionAndCrop(grayscale); 

            //parameter to  be passed to thread fun 
            f[i]={empty,grayscale};

            //create a thread along with appropriate parameters
            pthread_create(&t[i], NULL, fun, &f[i]); 

            // if i<num-1, increment i
            if(i<num-1){    
                i++;
            }

            // else, "num" threads have been created, wait for responses from each thread  
            else{
                for(int j=0;j<num;j++){
                    pthread_join(t[j],&density[j]); 
                    queueDensity.push_back(*(double*)density[j]);  
                }
                i=0;
            }
            
        }        

        count++;
        
    }
    int thread_remaining = 1148%num; 
    for(int j = 0; j< thread_remaining;j++){
        pthread_join(t[j],&density[j]); 
        queueDensity.push_back(*(double*)density[j]);  
    }
    //dynamic_density=queueDensity;
    auto stop = high_resolution_clock::now();
    write_csv("output4_"+to_string(num)+".csv", queueDensity, dynamic_density);
    auto duration = duration_cast<seconds>(stop - start);


    cout << "Time taken by function: "
         << duration.count() << " seconds" << endl;
    // cout << "Time taken by function: "
    //      << duration.count()/1000 << " seconds" << endl;
    // for(int i = 0; i < queueDensity.size(); i++){
    //      cout<<queueDensity[i]<<",";
    // }
    // cout<<endl;

    // for(int i = 0; i < dynamic_density.size(); i++){
    //     cout<<dynamic_density[i]<<",";
    // }
    // cout<<endl;

    // for(int i = 0; i < queueDensity.size(); i++){
    //     cout<<i<<",";
    // }
    
}

