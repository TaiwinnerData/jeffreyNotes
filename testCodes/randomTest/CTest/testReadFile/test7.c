#include <stdio.h>
#include <stdlib.h>


void main(){
	FILE *testFile = fopen("file.txt", "r");
	char buffChar[1000];

	fseek(testFile, 0, SEEK_END);
	int fileLen = ftell(testFile);
	printf("show the position of the file:\n");
	printf("%d\n", fileLen);
	fread(buffChar, sizeof(char), 1, testFile);
	printf("%s\n", buffChar);
	fclose(testFile);
}
