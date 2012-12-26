#include <stdio.h>
#include <math.h>

#define N 1000000

char primes[N / 8];
char numbers[N / 8] = {0};

int main(void)
{
	int p, b, n;

	/* Find primes using sieve of Eratosthenes */
	for (p = 0; p < N/8; ++p)
		primes[p] = 0xff;
	primes[0] = ~3;

	for (p = 2, n = (int) sqrt(n) + 1; p < n; ++p)
		if (primes[p/8] & 1 << (p%8))
			for (b = p << 1; b < N; b += p)
				primes[b/8] &= ~(1 << (b%8));


	/* Bruteforce Goldbach's conjecture 
	 *
	 *    Every odd number can be expressed as a prime, p, plus 2 times a 
	 *    square, b, where b can be any integer including 0.
	 *
	 *    p + 2 * b*b
	 */
	for (p = 0; p < N; ++p) {
		if (!(primes[p/8] & 1 << (p%8)))
			continue;

		for (b = 0; ((n = p + 2 * b*b) < N); ++b)
			numbers[n/8] |= 1 << (n % 8);

	}

	/* Print result */
	for (n = 3; n < N; n += 2)
		if (!(numbers[n/8] & 1 << (n%8)))
			printf("%d\n", n);

	return 0;
}
