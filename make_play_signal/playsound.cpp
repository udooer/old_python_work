#include <cstdlib>
#include <ctime>
#include <iostream>
#include <unistd.h>


void sleepinsecond(double);
int main(int argc, char* argv[])
{
	if(argc == 2){
		std::string path;
		path = argv[1];
		path = "aplay " + path; 		
		while(1){
			system(path.c_str());
			sleepinsecond(2);
			std::cout<<"sleep!\n";
		}
	}
	else{
		std::cout<<"command error!!\n";	
		std::cout<<"./*.o [absolute path]\n";
	}
	return 0; 
}
void sleepinsecond(double s)
{
	std::clock_t start = std::clock();
 	while(1)
		if((std::clock()-start)/(double)CLOCKS_PER_SEC > s)
			break;
}


