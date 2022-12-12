#include <stdio.h>
#include <stdlib.h>

void main(){
	int testNum = 1;
	int *a = &testNum;
	printf("%p\n", a);
	printf("%p\n", &testNum);
}
