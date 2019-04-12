# Writeup 7 - Binaries I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
printf("your code here");
```
#include <stdio.h>

int main(void) {
	int a = 0x1ceb00da;
	int b = 0xfeedface;

	printf("%d\n", a);

	printf("%d\n", b);

	a ^= b;
	b ^= a;
	a ^= b;

	printf("%d\n", a);

	printf("%d\n", b);
}


### Part 2 (10 Pts)

The program allocates space for 2 variables, where each variable is 4 bytes long. The program then assigns "0x1ceb00da" to one variable and "0xfeedface" to the other variable. The program then prints both variables. The program then swaps values of the variables and then prints both variables again.
