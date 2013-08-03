#include <cstdio>
#include <tr1/cstdint>
#include <cmath>

void sieve(int length, uint16_t* vector)
{
	int i, j, n, m;

	n = length; m = (int) sqrt(n);
	for (i = 0; i < length/16; ++i)
		vector[i] = 0xffff;

	for (i = 2; i < m; ++i)
		if (vector[i/16] & (1 << (i%16)))
			for (j = i << 1; j < n; j += i)
				vector[j/16] &= ~(1 << (j%16));
}


bool prime(int n, uint16_t* primes)
{
	return (primes[n/16] & (1 << (n%16))) != 0;
}


uint16_t digits(int number)
{
	uint16_t digits;

	for (digits = 0; number > 0; number /= 10)
		digits |= 1 << (number % 10);

	return digits;
}


int main(void)
{
	uint16_t* primes = new uint16_t[10000/16];

	sieve(10000, primes);

	for (int prime1 = 1000; prime1 < 10000; ++prime1)
	{
		if (prime(prime1, primes)) 
		{
			for (int prime2 = prime1 + 1; prime2 < 10000; ++prime2)
			{
				if (prime(prime2, primes) && digits(prime1) == digits(prime2))
				{
					int distance = prime2 - prime1;
					if (prime(prime2+distance, primes) && digits(prime2+distance) == digits(prime1))
					{
						printf("%d %d %d, %d\n", prime1, prime2, prime2+distance, distance);
					}
				}
			}
		}
	}

	delete primes;
	return 0;
}
