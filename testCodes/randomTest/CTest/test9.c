#include <stdio.h>
#include <stdlib.h>

void main(){
	int *test = (int *)malloc(sizeof(int)*3);
	printf("Show the memory of the dynamic memory test:\n");
	printf("%p\n", test);

	int testArray[4] = {1, 2, 3, 4};
	test = &testArray;
	printf("Show the pointer test[4]: %d\n", *test);
}
