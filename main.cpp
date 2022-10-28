/*
 *	Testing CPP header files using the source file defined in /headertest/ 
 */
#include <iostream>
#include "headertest/calculations.cpp"

int main(){
	std::cout << "The sum of 3 and 4 is: " << add(3, 4) << std::endl;
	std::cout << "The difference between 3 and 4 is: " << sub(3, 4) << std::endl;
	output_message("Import was successful");

	std::cout << "This text is native to main.cpp " << std::endl; 

}

