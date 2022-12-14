// This test can show that you can use pointer as array if you want in c Language.

#include <stdio.h>
#include <stdlib.h>

void main(){
	int test = 1;
	int *testPointer = &test;

	// Show the array of the test.
	for(int i=0; i<=9; ++i){
		printf("%d: ", i);
		printf("%d\n", testPointer[i]);
	}
}
