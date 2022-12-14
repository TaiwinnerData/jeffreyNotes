#include <stdio.h>
#include <stdlib.h>

int main(){
	char *testStr = (char *)malloc(15);
	testStr = "first test.";
	printf("%s\n", testStr);

	testStr = (char *)realloc(testStr, 30);
	//free(testStr);
	testStr = "This is second test.";
	printf("%s\n", testStr);
	free(testStr);
}


