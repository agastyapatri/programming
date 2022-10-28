/*
 *	CPP program to find the sum of the digits of a number
 *
 */
#include <iostream>

int exponent(int base, int exp){
	double power = 1;
	for(int i = 1; i<=exp; i++){
		power = power*base;}

	return power;
}

int main(){
	int N;
	int sum = 0;
	int count = 0;

	std::cout << "Enter any number: ";
	std::cin >> N;
	
	for(int i = 1; i < 5 ; i++){
		int num = N % exponent(10, i);
		sum += (num - count ) / (exponent(10, i)/10);
		count = sum;

		std::cout << num << " " << count << std::endl;
	}
}
