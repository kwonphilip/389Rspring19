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
	unsigned long arr[4];
	arr[1] = 0x1ceb00da;
	arr[0] = 0xfeedface;

	printf("%lx\n", arr[0]);

	printf("%lx\n", arr[1]);

	arr[0] ^= arr[1];
	arr[1] ^= arr[0];
	arr[0] ^= arr[1];

	printf("%lx\n", arr[0]);

	printf("%lx\n", arr[1]);
}


### Part 2 (10 Pts)

The program allocates space for an array of 4 elements, where each element is 4 bytes. The program then assigns 0xfeedface to the first element and 0x1ceb00da to the second element. The program then prints the first element and the second element. The program then swaps the first and second element (i.e. 0x1ceb00da is now the first element and 0xfeedface is now the second element) before printing the elements again.
