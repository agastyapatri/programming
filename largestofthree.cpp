/*
 *	C++ program to find the largest of 3 numbers 
 */
#include <iostream>
int main(){
	int a, b, c;
	int max = 0;
	std::cout << "Enter any three numbers: ";
	std::cin >> a >> b >> c;
	
	if (a > b){
		if(a > c){max = a;}
		else{max = c;}
	} 
	else if (b > a){
		if(b > c){max = b;}
		else{max = c;}
	}

	std::cout << "The largest of " << a << ", " << b << ", and " << c << " is " << max << std::endl; 
}
