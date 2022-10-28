/*
 *	CPP program to print the fibonacci sequence 
 */
#include <iostream>
 
int main(){
	int N;
	std::cout << "Enter the number up to which the sequence is desired: ";
	std::cin >> N;
	int t1 = 0;
	int t2 = 1;

	int fib = 0;


	for(int i=1; i < N; i++){
		fib = t1 + t2;
		t1 = t2;
		t2 = fib;
		
		std::cout << fib << " ";

	}
	std::cout << std::endl;
}
