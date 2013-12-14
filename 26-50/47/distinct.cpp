#include <vector>
#include <cstdio>

#define LIMIT 100000
#define TARGET 4

using namespace std;



vector<int> primes;



void sieve(int n)
{
	int* numbers = new int[n];

	for (int i = 0; i < n; ++i)
	{
		numbers[i] = i;
	}

	for (int i = 2; i < n; ++i)
	{
		if (numbers[i] != 0)
		{
			primes.push_back(i);
			for (int j = i << 1; j < n; j += i)
			{
				numbers[j] = 0;
			}
		}
	}

	delete[] numbers;
}



int num_prime_factors(int k)
{
	int divisors = 0, remainder = k;

	for (vector<int>::iterator prime = primes.begin(); remainder > 1 && prime != primes.end(); prime++)
	{
		if (*prime * *prime > k)
		{
			return ++divisors;
		}

		if (remainder % *prime == 0)
		{
			++divisors;
			
			do
			{
				remainder /= *prime;
			} 
			while (remainder % *prime == 0);
		}
	}

	return divisors;
}



int main(void)
{
	sieve(LIMIT);

	int n = 0;
	int step = 1;

	while (n < TARGET)
	{
		if (num_prime_factors(step) >= TARGET)
		{
			++n;
		}
		else
		{
			n = 0;
		}

		++step;
	}

	printf("%d\n", step - TARGET);

	return 0;
}
