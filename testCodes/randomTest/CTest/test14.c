#include <stdio.h>
#include <stdlib.h>

void main(){
	FILE *f = fopen("test.txt", "r");
	if (f == NULL){
		printf("pointer set fail.");
	}
	else {
		printf("Show the file pointer: %p\n", f);
	}
}

