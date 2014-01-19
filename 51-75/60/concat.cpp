#include <cstdio>
#include <vector>
#include <cmath>

#define TARGET 5
#define LIMIT 30000

std::vector<unsigned> primes;
std::vector<bool> numbers;



inline bool is_prime(unsigned x)
{
	if (x < numbers.size())
	{
		return numbers[x];
	}

	for (unsigned i = 2; i <= (unsigned) sqrt(x) + 1; ++i)
	{
		if (x % i == 0)
		{
			return false;
		}
	}

	return true;
}



inline void print_set(const std::vector<unsigned>& set)
{
	unsigned sum = 0;
	for (std::vector<unsigned>::const_iterator i = set.begin(); i != set.end(); ++i)
	{
		printf("%u  ", *i);
		sum += *i;
	}
	printf("= %u\n", sum);
}



inline unsigned concat(unsigned a, unsigned b)
{
	int p, k;
	for (p = 1, k = b; k > 0; k /= 10, p *= 10);
	return a * p + b;
}



void sieve(unsigned N)
{
	for (unsigned i = 0; i < N; ++i)
	{
		numbers.push_back(true);
	}

	numbers[0] = false;
	numbers[1] = false;
	for (unsigned i = 2; i < N; ++i)
	{
		if (numbers[i])
		{
			primes.push_back(i);
			for (unsigned j = i << 1; j < N; j += i)
			{
				numbers[j] = false;
			}
		}
	}
}



inline bool verify(const std::vector<unsigned>& set, unsigned x)
{
	for (std::vector<unsigned>::const_iterator i = set.begin(); i != set.end(); ++i)
	{
		if (!is_prime(concat(*i, x)) || !is_prime(concat(x, *i)))
		{
			return false;
		}
	}

	return true;
}



inline void test(std::vector<unsigned>& set, std::vector<unsigned>::const_iterator p)
{
	
	while (p != primes.end())
	{
		if (verify(set, *p))
		{
			set.push_back(*p);

			if (set.size() == TARGET)
			{
				print_set(set);
			}
			else
			{
				std::vector<unsigned>::const_iterator i = p;
				test(set, ++i);
			}
			
			set.pop_back();
		}

		++p;
	}
}




int main()
{
	puts("Calculating primes...");
	sieve(LIMIT);

	puts("Finding prime pair sets...");
	std::vector<unsigned> set;

	for (std::vector<unsigned>::const_iterator p = primes.begin(); p != primes.end(); ++p)
	{
		set.clear();
		set.push_back(*p);
		std::vector<unsigned>::const_iterator i = p;
		test(set, ++i);
	}

	puts("Done");
	return 0;
}
