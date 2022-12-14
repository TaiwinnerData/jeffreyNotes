#include <stdio.h>
#include <stdlib.h>

void main(){
	int number;
	char line[100];
	FILE *f = fopen("test.txt", "r"); 
	if (f == NULL)
	{
		printf("Error! Can't open the file!\n");
		exit(-1);
	}

	// Attempt to read the line and store the value in the number variable.

	
	while (fscanf(f, "%s", & line) == 1)
	{
		printf("the line: %s\n", line);
	}
		
}
