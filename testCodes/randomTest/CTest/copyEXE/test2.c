#include <stdio.h>
#include <stdlib.h>

// Read whole file test.
void main(){
	
	char wholeFile[10000];
	// copy from
	FILE *fileTest = fopen("file.txt", "r");
	// copy to
	FILE *fileTest2 = fopen("file2.txt", "wb");

	fseek(fileTest, 0, SEEK_END);
	int fileSize = ftell(fileTest);
	printf("Show the size of file size: %d\n", fileSize);
	char *buffChars = (char *)malloc(sizeof(char)*fileSize);

	// read wholeFile array to buff.
	for(int i=0; i<fileSize; ++i){
		fscanf(fileTest, "%c", &buffChars[i]);
	}

	// show the read result
	for(int i=0; i<fileSize; ++i){
		printf("show buffChars[%d]: %c", i, buffChars[i]);
	}


	// write wholeFile array to file2.txt
	
	for(int i=0; i<fileSize; ++i){
		fprintf(fileTest2, "%c", buffChars[i]);
	}
	



	fclose(fileTest);
	fclose(fileTest2);


}
