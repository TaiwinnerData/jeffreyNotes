#include <stdio.h>
#include <stdlib.h>

int bubbleSort(int *array, int array_len){
	for(int i=0; i<array_len; ++i){
		for(int j=0; j<array_len-1-i; ++j){
			if(array[j] > array[j+1]){
				int temp_value = array[j];
				array[j] = array[j+1];
				array[j+1] = temp_value;
			}
		}
	}
	return 0;
}

void main(){
	int testArray[10] = {3, 4, 5, 1, 143, 2, 6, 8, 6, 20};
	bubbleSort(testArray, 10);
	// show the testArray with bubbleSort.
	for(int i; i<10; ++i){
		printf("testArray[%d]: %d\n", i, testArray[i]);
	}
}
