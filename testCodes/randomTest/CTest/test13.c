#include <stdio.h>
#include <stdlib.h>

void main(){
	int array_len = 11;
	int array_len_2 = 20;
	int *test;
	test = (int *)malloc(sizeof(int)*array_len);

	// put the value into the array
	for(int i=0; i<=array_len; ++i){
		test[i] = i*10;
	}

	// Show the value inside the array
	for(int i=0; i<=array_len; ++i){
		printf("%d\n", test[i]);
	}


	test = realloc(test, sizeof(int)*array_len_2);
	// set the value of the array.
	for(int i=0; i<=array_len_2; ++i){
		test[i] = i*20;
	}

	// Show the value of the array.
	for(int i=0; i<=array_len_2; ++i){
		printf("%d\n", test[i]);
	}
	free(test);
	
}
