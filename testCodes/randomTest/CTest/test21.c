#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct person {
	char name[50];
	int id;
};

void main(){
	struct person Peter;
	strcpy(Peter.name, "test");
	Peter.id = 1;

	printf("Show Peter's name: %s\n", Peter.name);
	printf("Show Peter's id: %d\n", Peter.id);
}


