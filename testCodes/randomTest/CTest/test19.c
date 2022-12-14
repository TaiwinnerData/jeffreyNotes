// this test is for testing if pointer variable can be redeclare or not.
#include <stdio.h>
#include <stdlib.h>


void main(){
	int *testInt;
	int b = 1;
	int c = 2;
	testInt = &b;
	testInt = &c;

	printf("show the testInt value: %d\n", *testInt);

}
