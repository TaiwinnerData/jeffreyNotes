#include <stdio.h>
#include <stdlib.h>

void main(){
	FILE *testFile;
	testFile = fopen("testRead.txt", "r");

	int testChars[30];

/*
	for(int i=0; i<16; ++i){


	}
	*/
	
	/*
	fscanf(testFile, "%d\n", &testChars[0]);
	fscanf(testFile, "%d\n", &testChars[1]);
	fscanf(testFile, "%d\n", &testChars[2]);
	*/

	for(int j=0; j<30; ++j){
		fscanf(testFile, "%d\n", &testChars[i]);
	}
	fclose(testFile);


	//show all the characters in testChars.
	for(int i=0; i<30; ++i){
		printf("testChars[%d]: %d\n", i, testChars[i]);

	}



}

