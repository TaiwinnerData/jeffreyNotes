// This test is for testing the pointer properties of array.
#include <stdio.h>
#include <stdlib.h>

void main(){
	int testArray[3] = {1, 2, 3};

	int *testArray_p = testArray;
	printf("%p\n", testArray_p);
	int *testArray_p_2 = &testArray;
	printf("%p\n", testArray_p_2);

	printf("--------------\n");
	printf("%d\n", *(testArray_p+3));

	printf("--------------\n");
	printf("%d\n", *(testArray_p_2+3));


}
