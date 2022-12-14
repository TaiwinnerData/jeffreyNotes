#include <stdio.h>
#include <stdlib.h>

void main(){
	// open the file you want to read
	FILE *f = fopen("test.txt", "r");
	// create the words 2d array to store the data.
	char words[100][100];

	// read the character from test.txt file
	fscanf(f, "%s", words[0]);
	fscanf(f, "%s", words[1]);
	fscanf(f, "%s", words[2]);
	printf("Show words[0]: %s\n", words[0]);
	printf("Show words[0]: %s\n", words[1]);
	printf("Show words[0]: %s\n", words[2]);
	fclose(f);

	// use another poiner to open the same file.
	f = fopen("test.txt", "r");
	// create the words 2d array to store the data.
	char words_2[100][100];

	// read the character from test txt file.
	fscanf(f, "%s", words_2[0]);
	printf("Show words_2[0]: %s\n", words_2[0]);





}
