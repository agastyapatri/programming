/*
 *	CPP program to print the pascals triangle
 */
#include <iostream>

int factorial(int n){
	// function to calculate the factorial of a number
	double fact = 1;
	for(int i = 1; i <= n; i++){
		fact = fact*i;
	}
	return fact;
}

int nCr(int n, int r){
	return  factorial(n) / ( factorial(r)*factorial(n-r));  

}



int main(){
	// Each row of the pascal's triangle is the nCr coefficients with row_no = n
	int N;
	std::cout << "Enter the number of rows desired: ";
	std::cin >> N;
	
	std::cout << 1 << std::endl;
	for(int i = 1; i <=N; i++ ){
		for(int j = 0; j <=i; j++){
			std::cout << nCr(i, j) << " ";
		} 
		std::cout << std::endl;
	}
}
