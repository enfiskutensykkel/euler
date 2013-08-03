#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <stdint.h>

#define N 10000000


int pandigital(int32_t number)
{
	/* A map over used digits */
	uint16_t digits[10] = {0};
	uint16_t len;

	/* For each digit, check if used no more than once */
	digits[0] = 1;
	for (len = 1; number > 0; number /= 10, ++len)
		if (++digits[number % 10] > 1)
			return 0;

	/* For each digit, check if used at least once */
	while (len)
		if (digits[--len] != 1)
			return 0;

	return 1;
}



void sieve(int32_t length, uint8_t *vector)
{
	int32_t i, j, n, m;

	/* Initialize array */
	n = length; m = (int32_t) sqrt(n);
	for (i = 0; i < length/8; ++i)
		vector[i] = 0xff;

	/* Do sieve of Eratosthenes */
	for (i = 2; i < m; ++i)
		if (vector[i/8] & (1 << (i%8)))
			for (j = i << 1; j < n; j += i)
				vector[j/8] &= ~(1 << (j%8));
}



int main(void)
{
	uint8_t* bitmap = malloc(N / 8);

	/* Find primes */
	sieve(N, bitmap);

	/* Loop through primes and find out if their pandigital */
	int32_t i;
	int32_t largest = 1;
	for (i = 2; i < N; ++i)
		if ((bitmap[i / 8] & (1 << (i%8))) && pandigital(i))
			largest = i;

	printf("%d\n", largest);

	free(bitmap);
	return 0;
}
