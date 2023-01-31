#include <stdio.h>
#include <stdlib.h>

// Read whole file test.
void main(){
	char wholeFile[10000];
	// copy from
	FILE *fileTest = fopen("file.txt", "r");
	// copy to
	FILE *fileTest2 = fopen("file2.txt", "wb");

	for(int i=0; i<10000; ++i){
		fscanf(fileTest, "%c", &wholeFile[i]);
	}


	// Show wholeFile array content.
	/*
	for(int i=0; i<10000; ++i){
		printf("show wholeFile[%d]: %c\n", i, wholeFile[i]);
	}
	*/

	// write wholeFile array to file2.txt
	for(int i=0; i<10000; ++i){
		fprintf(fileTest2, "%c", wholeFile[i]);
	}



	fclose(fileTest);
	fclose(fileTest2);


}
