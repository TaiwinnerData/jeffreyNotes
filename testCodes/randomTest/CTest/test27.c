#include <stdio.h>

void main(){
	union abc {
		int x;
		char ch;
	} var;

	var ch = 'A';
	printf("%d", var.x);
}
