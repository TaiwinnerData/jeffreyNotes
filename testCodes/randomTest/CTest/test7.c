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
	int *arrayTest2[3];
	int a = 1;
	int b = 2;
	int c = 3;
	arrayTest2[0] = &a;
	arrayTest2[1] = &b;
	arrayTest2[2] = &c;


	for(int i = 0; i<=2; ++i){
		printf("%d\n", *arrayTest2[i]);
	}

}
	
