#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct person{
	char name[50];
	int id;
} person;

void main(){
	person Peter;
	strcpy(Peter.name, "Test");
	Peter.id = 1;
	printf("Show the name of Peter: %s\n", Peter.name);
	printf("Show the id of Peter: %d\n", Peter.id);

}


