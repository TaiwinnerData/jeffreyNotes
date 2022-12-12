// Test if c language can over the range of the array.
#include <stdio.h>
#include <stdlib.h>

void main(){
	int testArray[3] = {1, 2, 3};
	testArray[3] = 10;
	testArray[4] = 20;
	printf("%d\n", testArray[3]);
	printf("%d\n", testArray[4]);
}
