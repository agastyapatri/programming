/*
 *	CPP Program to print the LCM of two numbers
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
	
	// FINDING THE LCM OF THE TWO NUMBERS
	int HCF;
	for(int i = 1; i < greater ; i++){
		if((smaller % i == 0 ) && (greater%i == 0)){
			HCF = i;
		}
	}
	

	// FINALLY FINDING THE LCM
	int LCM;
	if (greater % smaller == 0){
		LCM = greater;
	}
	else{
		LCM = (greater*smaller)/HCF;
	}
	std::cout << "The LCM of " << a << " and " << b << " is: " << LCM << std::endl;

}




