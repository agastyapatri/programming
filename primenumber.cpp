/*
 *	CPP program to check if a given number is prime or not
 */
#include <iostream>
int main(){
	int N;
	int num_factors=0;

	std::cout << "Enter a number: ";
	std::cin >> N;

	for(int i = 1; i <= N; i++){
		if(N%i == 0){num_factors++;}
	}

	if(num_factors > 2){std::cout << N << " is a composite number" << std::endl;}
	else{std::cout << N << " is a prime number" << std::endl;}
}
