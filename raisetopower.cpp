/*
 * CPP program to raise any given number X to the power of N 
 * */

#include <iostream>
int main(){
	int X, N;
	double sol;
	std::cout << "Enter any number: ";
	std::cin >> X;
	std::cout << "Enter the exponent: ";
	std::cin >> N;
	
	sol = 1;
	for(int i=1; i<N+1; i++){
		sol *= X;
	}
	std::cout << X  << " to the power of " << N << " is: " << sol << std::endl;  
	

}
