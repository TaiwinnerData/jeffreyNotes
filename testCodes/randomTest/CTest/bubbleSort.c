// This script is for testing bubble sort method.
#include <stdio.h>
#include <stdlib.h>


int bubbleSort(int *testArray){
	//int len_of_array = sizeof(*testArray)/sizeof(int);
	int len_of_array = 10;
	for(int i=0; i<len_of_array; ++i){
		for(int j=0; j<len_of_array-i-1; ++j){
			if(testArray[j] > testArray[j+1]){
				int temp_value = testArray[j];
				testArray[j] = testArray[j+1];
				testArray[j+1] = temp_value;
			}
		}
	}
}


void main(){
	int testArray[10] = {5, 1, 7, 2, 3, 7, 22, 1, 78, 11};
	bubbleSort(testArray);
	// show testArray
	for(int i=0; i<10; ++i){
		printf("testArray[%d]: %d\n", i, testArray[i]);
	}
}
