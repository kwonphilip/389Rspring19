/*
 * Name: Philip Kwon
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Philip Kwon
 */

/* your code goes here */
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