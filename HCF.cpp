/*
 *	CPP Program to display the HCF of two numbers
 */
#include <iostream>
int main(){
	int a, b;
	std::cout << "Enter the two numbers: ";
	std::cin >> a >> b;
	
	//Finding the HCF of the two numbers:
	int greater, smaller;

	if(a > b){
		greater = a;
		smaller = b;
	}
	else{
		greater = b;
		smaller = a;
	}
	
	int HCF;
	for(int i = 1; i < greater ; i++){
		if((smaller % i == 0 ) && (greater%i == 0)){
			HCF = i;
		}
	}
	std::cout << "HCF of " << a << " and  " << b << " is: " << HCF << std::endl; 

}
