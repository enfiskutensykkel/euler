#include <cstdio>
#include <set>
#include <list>

using namespace std;


set<long> primes;


void generate_primes(const long limit) 
{
	char* numbers = new char[limit >> 3];

	for (long i = 0; i < (limit >> 3); ++i)
		numbers[i] = 0xff;

	for (long i = 2; i < limit; ++i) 
	{
		if (numbers[i >> 3] & (1 << (i & 7))) 
		{
			primes.insert(i);

			for (long j = i << 1; j < limit; j += i)
				numbers[j >> 3] &= ~(1 << (j & 7));
		}
	}

	delete[] numbers;
}

void generate_masks(list<int>& masks, const int digits)
{
	const int max = 1 << digits;
	for (int i = 1; i < max; ++i)
	{
		masks.push_back(i);
		masks.push_back(max - i);
	}
}

inline int count_digits(long number)
{
	int digits = 0;
	while (number)
	{
		number /= 10;
		++digits;
	}
	return digits;
}

inline int replace_digits(long number, int mask, int digit)
{
	list<int> digits;
	while (number)
	{
		digits.push_front(number % 10);
		number /= 10;
	}

	int i;
	list<int>::iterator it;

	int j = 0, k = 0;

	for (i = 0, it = digits.begin(); it != digits.end(); ++it, ++i)
	{
		if (mask & (1 << i))
		{
			++j;
			k += *it == digit;
			*it = digit;
		}
	}

	if (j != k && k != 0)
		return -1;

	for (i = 0, it = digits.begin(); it != digits.end(); ++it)
		i = 10 * i + *it;

	return i;
}

void find_family(long prime, set<long>& family, int mask)
{
	const int digits = count_digits(prime);

	for (int i = 0; i < 10; ++i)
	{
		const long r = replace_digits(prime, mask, i);

		if (r != -1 && count_digits(r) == digits && primes.find(r) != primes.end())
			family.insert(r);
	}
}

int main(void)
{
	generate_primes(1000000);
	const unsigned long target_length = 8;

	for (long prime: primes)
	{
		list<int> masks;
		generate_masks(masks, count_digits(prime));

		for (int mask: masks)
		{
			set<long> family_members;
			find_family(prime, family_members, mask);
			
			if (family_members.size() >= target_length)
			{
				printf("%ld: %lu\n", prime, family_members.size());
				for (long member: family_members)
				{
					printf("  %ld\n", member);
				}

				return 0;
			}

		}
	}

	return 1;
}
