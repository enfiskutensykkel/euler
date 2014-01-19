#include <cstdio>
#include <vector>
#include <cmath>

#define TARGET 5
#define NUMBERS 100000000

std::vector<bool> numbers;




inline void print_set(const std::vector<unsigned>& set)
{
	unsigned sum = 0;
	for (auto i = set.begin(); i != set.end(); ++i)
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
	for (unsigned i = 2; i < (unsigned) sqrt(N) + 1; ++i)
	{
		for (unsigned j = i << 1; numbers[i] && j < N; j += i)
		{
			numbers[j] = false;
		}
	}
}



inline bool verify(const std::vector<unsigned>& set, unsigned x)
{
	const unsigned lim = numbers.size();

	for (auto i = set.begin(); i != set.end(); ++i)
	{
		unsigned v = concat(*i, x);
		unsigned w = concat(x, *i);
		if (v >= lim || w >= lim || !numbers[v] || !numbers[w])
		{
			return false;
		}
	}

	return true;
}



inline void test(std::vector<unsigned>& set)
{
	const unsigned lim = numbers.size();

	for (unsigned i = set.back() + 1; i < (unsigned) sqrt(lim) + 1; ++i)
	{
		if (numbers[i] && verify(set, i))
		{
			set.push_back(i);
			if (set.size() == TARGET)
			{
				print_set(set);
			}
			else
			{
				test(set);
			}
			set.pop_back();
		}
	}
}




int main()
{
	puts("Calculating primes...");
	sieve(NUMBERS);

	puts("Finding prime pair sets...");
	std::vector<unsigned> set;

	for (unsigned i = 3; i < (unsigned) sqrt(numbers.size()) + 1; ++i)
	{
		if (numbers[i])
		{
			set.clear();
			set.push_back(i);
			test(set);
		}
	}

	puts("Done");
	return 0;
}
