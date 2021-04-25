in: compile 
	 
compile:
	g++ part1_b_new.cpp -o out -std=c++11 `pkg-config --cflags --libs opencv`
	
one: 
	g++ method1.cpp -o out -std=c++11 `pkg-config --cflags --libs opencv`

two:
	g++ method2.cpp -o out -std=c++11 `pkg-config --cflags --libs opencv`
	
three:
	g++ method3.cpp -o out -std=c++11 `pkg-config --cflags --libs opencv`
	
four:
	g++ method4.cpp -o out -std=c++11 `pkg-config --cflags --libs opencv`
		
clean:
	rm -rf out Warped_Source_Image.jpg Cropped_Image.jpg output.csv output4.csv
