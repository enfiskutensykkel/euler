#include <stdio.h>
#include <stdint.h>
#include <math.h>

/* This is a horrible solution, which just bruteforces its way
 * to the correct answer.
 */

#define N 28123

uint8_t primes[N / 8];
uint8_t abundant[N / 8] = {0};
uint8_t summap[N / 8] = {0};

void sieve(void)
{
	int i, j, n;

	for (i = 0; i < N/8; ++i)
		primes[i] = 0xff;

	for (i = 2, n = (int) sqrt(N); i < n; ++i)
		if (primes[i/8] & 1 << (i%8))
			for (j = i << 1; j < N; j += i)
				primes[j/8] &= ~(1 << (j%8));	
}

int sum(int k)
{
	int i, n;

	if (k == 1)
		return 1;
	else if (primes[k/8] & 1 << (k%8))
		return 1;

	for (n = 0, i = 1; i < k/2+1; ++i)
		if (k % i == 0)
			n += i;

	return n;
}

int main(void)
{
	int i, j;

	sieve();

	for (i = 1; i < N; ++i)
		if (sum(i) > i)
			abundant[i/8] |= 1 << i%8;

	for (i = 1; i < N; ++i) {
		if (!(abundant[i/8] & 1 << (i%8)))
			continue;

		for (j = 1; j < N; ++j) {
			if (!(abundant[j/8] & 1 << (j%8)))
				continue;

			if (i + j < N)
				summap[(i+j) / 8] |= 1 << (i+j)%8;
		}
	}

	for (i = 1, j = 0; i < N; ++i)
		if (!(summap[i/8] & 1 << (i%8)))
			j += i;

	printf("%d\n", j);
	return 0;
}
