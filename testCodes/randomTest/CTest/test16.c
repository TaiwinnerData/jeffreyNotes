#include <stdio.h>
#include <stdlib.h>

void main(){
	// Create an 2d array to store the chars in test.txt file.
	char words[100][100];

	// Read the data from file test.txt.
	FILE *f = fopen("test.txt", "r");
	// Check if the file is opened or not.
	if (f == NULL){
		printf("Error! The file is not opened.\n");
	}


	// The most simple way to store the data value is like below.
	fscanf(f, "%s", words[0]);
	fscanf(f, "%s", words[1]);
	fscanf(f, "%s", words[2]);
	fscanf(f, "%s", words[3]);

	printf("words1: %s\n", words[0]);
	printf("words2: %s\n", words[1]);
	printf("words3: %s\n", words[2]);
	printf("words4: %s\n", words[3]);

	// But i can use another way to do this.
	
	



}
