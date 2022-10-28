/*
 *	CPP program to find the sum of first n natural numbers
 */
#include <iostream>
int main(){
	int N;
	std::cout << "Enter a number: ";
	std::cin >> N;

	std::cout << "The sum of natural numbers up to " << N << " is " << N*(N+1)/2 << std::endl; 

}	
