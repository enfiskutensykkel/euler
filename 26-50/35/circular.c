#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* find all primes below 10^6 using sieve of Eratosthenes */
void sieve(int len, char *map)
{
	int i, j, n, m;

	for (i = 0; i < len; ++i)
		map[i] = 0xff;

	n = len * 8; m = (int) sqrt(n);
	for (i = 2; i < m; ++i)
		if (map[i/8] & (1 << (i%8)))
			for (j = i << 1; j < n; j += i)
				map[j/8] &= ~(1 << (j % 8));
}


/* test if all rotations of a number is prime (circular prime) */
int rot(int x, char *primes)
{
	int i, j, k, n, *digits;

	/* count digits */
	for (n = 0, i = x; i > 0; i /= 10)
		++n;

	/* store digits in array */
	digits = malloc(sizeof(int) * n);
	for (k = n, i = x; i > 0; i /= 10)
		digits[--k] = i % 10;

	/* rotate */
	for (i = 0; i < n; ++i) {
		for (x = k = 0, j = i; k < n; ++k, j = (j + 1) % n) {
			x = 10 * x + digits[j];
		}

		/* test for primality */
		if (!(primes[x/8] & (1 << (x % 8)))) {
			free(digits);
			return 0;
		}
	}

	free(digits);
	return 1;
}


int main(void)
{
	char *bitmap = malloc(1000000/8+1);
	int i, n;

	sieve(1000000/8, bitmap);

	for (n = 0, i = 2; i < 1000000; ++i) {
		if (bitmap[i/8] & (1 << (i % 8)))
			n += rot(i, bitmap);
	}

	printf("%d\n", n);

	free(bitmap);
	return 0;
}
