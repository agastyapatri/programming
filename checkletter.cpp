/*
 *	CPP program to check if a letter is a vowel or a consonant
 */
#include <iostream>
int main(){
	char letter;
	char vowels[] = "aeiou";
	std::cout << "Enter a letter: ";
	std::cin >> letter;
	
	for(int i=0; i<5; i++){
		if(vowels[i] == letter){
			std::cout << letter << " is a vowel"  << std::endl;
			return 0;
		}
	}
	std::cout << letter << " is a consonant" << std::endl; 
}


