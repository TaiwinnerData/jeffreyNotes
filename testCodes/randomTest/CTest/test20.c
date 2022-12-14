// this test is for testing write data into file
#include <stdio.h>
#include <stdlib.h>

void main(){
	char buf[100][100];
	printf("please input a string which lengh is smaller than 100: \n");
	scanf("%s", buf[0]);

	FILE *f = fopen("testWrite.txt", "w");
	// check if the file is open correctly.
	if (f == NULL){
		printf("Error! The file is not opened correctly.");
	}


	fprintf(f, "%s\n", buf[0]);
	fclose(f);

}
