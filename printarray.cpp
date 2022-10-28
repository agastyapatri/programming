#include <iostream>

int printArray(int n, int A[]){
	for(int i = 0; i < n; i++){\
		std::cout << A[i] << " ";
	}
	std::cout << std::endl;
	return 0;
}


int main(){
	int num_dims = 2;
	int A[num_dims] = {3,4};
	printArray(num_dims, A);
}
