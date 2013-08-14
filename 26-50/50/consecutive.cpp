#include <cstdio>
#include <vector>
#include <algorithm>

#define N 1000000

using std::vector;


void sieve(vector<int>& primes)
{
	bool prime_numbers[N] = {true, true, false};

	for (int i = 2; i < N; ++i)
	{
		if (!prime_numbers[i])
		{
			primes.push_back(i);
			for (int j = i << 1; j < N; j += i)
			{
				prime_numbers[j] = true;
			}
		}
	}
}

void cumulative(vector<int>& primes, vector<int>& sum)
{
	vector<int>::iterator i = primes.begin(); 
	int x = 0;
	
	while (i != primes.end())
	{
		x += *i;
		sum.push_back(x);
		i++;
	}
}

int main(void)
{
	vector<int> primes;
	sieve(primes);
	vector<int> cums;
	cumulative(primes, cums);

	int max = 0, n = 0;
	for (int i = 0; i < (int) primes.size(); ++i)
	{
		for (int j = i-1; j >= 0; --j)
		{
			if (cums[i] - cums[j] > N)
				break;

			if (i - j > n && std::binary_search(primes.begin(), primes.end(), cums[i] - cums[j]))
			{
				n = i - j;
				max = cums[i] - cums[j];
			}
		}
	}

	printf("Largest prime: %d\nSum of %d primes\n", max, n);
	return 0;
}
