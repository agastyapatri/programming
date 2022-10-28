/*
 *	CPP program to find the factorial of a given number 
 */
#include <iostream>
int main(){
	int N;
	double fact = 1;
	std::cout << "Enter a number: ";
	std::cin >> N;

	for(int i =1; i<=N; i++){
		fact = fact*i;
	}
	
	std::cout << "The Factorial of " << N << " is: " << fact << std::endl;


}
