// This test is for testing poiner of an array.
//
#include <stdio.h>
#include <stdlib.h>

void main(){
	// arrayPointer is the a pointer to stored the address of an array
	int arrayTest[3] = {1, 2, 3};
	int (*arrayPointer)[3] = &arrayTest;
	printf("%p\n", arrayPointer);
	printf("--------------\n");

	// array pointer is the pointer array to stored multiple array into array.
	int arrayTest2[3] = 
}
	
