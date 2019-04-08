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
	unsigned long arr[4];
	arr[1] = 0x1ceb00da;
	arr[0] = 0xfeedface;

	printf("%ld\n", arr[0]);

	printf("%ld\n", arr[1]);

	arr[0] ^= arr[1];
	arr[1] ^= arr[0];
	arr[0] ^= arr[1];

	printf("%ld\n", arr[0]);

	printf("%ld\n", arr[1]);
}