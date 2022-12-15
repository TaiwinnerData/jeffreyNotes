// This test is for testing how struct pointer works.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct person{
	char name[50];
	int age;
} person;


void main()
{
	person *Peter = (person *)malloc(sizeof(person));
	Peter -> age = 3;
	strcpy(Peter -> name, "Test");
	printf("Show Peter's name: %s\n", Peter -> name);
	printf("Show Peter's age: %d\n", Peter -> age);
}
