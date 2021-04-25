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


using namespace cv;
using namespace std;
using namespace std::chrono;

vector<Point2f> pts_src;
int n=0;
Mat im_src, h;
vector<Point2f> pts_dst;
Rect box;

void write_csv(string filename, vector<double> queueDensity, vector<double> dynamicDensity){
    //if(queueDensity.size()!=dynamicDensity.size()){
    //    cout << "Incompatible vectors" << endl;
    //    return ;
    //}
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


int main(int argc, char* argv[])
{    

    if(argc!=2){
        cout << "Incorrect command line input" << endl;
        return -1;
    }

    int x = stoi(argv[1]);

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

    Mat empty;
    empty = imread("empty.jpg", IMREAD_GRAYSCALE);
    //cout << "Empty has "<<empty.cols<<" columns and "<<empty.rows<<" rows."<<endl;
    empty = angleCorrectionAndCrop(empty);
    //cout << "Empty cropped has "<<empty.cols<<" columns and "<<empty.rows<<" rows."<<endl;
    //imshow("cropped empty road",empty);
    //waitKey(0);

    VideoCapture cap("trafficvideo.mp4");
    if(!cap.isOpened()){
        cout << "Error opening video stream or file" << endl;
        return -1;
    }

    int count = 0;

    Mat prev;

    /// queue/dynamic density of previous frame
    double queue_prev=0, dynamic_prev=0; 

    vector<double> dynamic_density;
    dynamic_density.push_back(0.1);
    vector<double> queueDensity;    
    vector<int> correspoding_frame;

    Mat frame, grayscale;
    int proc_count =0;

    while(true){
        // Capture frame-by-frame
        cap>>frame;

        // If the frame is empty, break immediately
        if (frame.empty())
            break;  

        // processing every 5th frame
        if(count%5 == 0){


            if(count%(5*x)==0){
                cvtColor(frame, grayscale, COLOR_BGR2GRAY);
                grayscale = angleCorrectionAndCrop(grayscale);
                queue_prev=q_density(grayscale, empty);
                //cout << "processing for the "<<proc_count<<"th time"<<endl;
                proc_count++;
            }
               
                queueDensity.push_back(queue_prev);

        }        

        count++;
        
    }
    auto stop = high_resolution_clock::now();
    write_csv("output1_"+to_string(x)+".csv", queueDensity, dynamic_density);
    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Time taken by function: "
         << duration.count()/1000000 << " seconds" << endl;
    // for(int i = 0; i < queueDensity.size(); i++){
    //     cout<<queueDensity[i]<<",";
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

