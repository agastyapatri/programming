/*
 *	C++ program to find the square root of a number
 */
#include <iostream>

int main(){
	int N;
	float root = 0;
	std::cout << "Enter a number: ";
	std::cin >> N;
	
	for(int i = 1; i <= N; i++){
		if(i*i == N){root = i;}
	}
	
	std::cout << "The Square root of " << N << " is: " << root << std::endl;
}
