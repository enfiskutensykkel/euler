#include <iostream>
#include <set>

#define TARGET 10000000

std::set<int>* factors[TARGET];
int numbers[TARGET];

int phi(int n)
{
	for (int k : *factors[n])
	{
		n -= n / k;
	}
	return n;
}

void count_digits(int n, int* digits)
{
	for (int i = 0; i < 10; ++i)
	{
		digits[i] = 0;
	}

	while (n > 0)
	{
		int digit = n % 10;
		n /= 10;
		++digits[digit];
	}
}

bool perm(int a, int b)
{
	int digits_a[10];
	int digits_b[10];
	
	count_digits(a, digits_a);
	count_digits(b, digits_b);

	for (int i = 0; i < 10; ++i)
	{
		if (digits_a[i] != digits_b[i])
		{
			return false;
		}
	}

	return true;
}

int main()
{
	numbers[0] = 0;
	numbers[1] = 0;
	for (int i = 2; i < TARGET; ++i)
	{
		numbers[i] = i;
	}

	factors[1] = new std::set<int>;
	factors[1]->insert(1);
	
	// Sieve of Eratosthenes to speed up the factorization
	for (int i = 0; i < TARGET; ++i)
	{
		if (numbers[i] != 0)
		{
			factors[i] = new std::set<int>;
			factors[i]->insert(i);

			for (int j = i << 1; j < TARGET; j += i)
			{
				numbers[j] = 0;
				if (factors[j] == nullptr)
				{
					factors[j] = new std::set<int>;
				}
				factors[j]->insert(i);
			}
		}
	}

	// Find factors of all non-prime numbers
	for (int i = 4; i < TARGET; ++i) 
	{
		if (!factors[i])
		{
			for (int k = 2, n = i >> 1; k <= n; ++k)
			{
				if (n % k == 0)
				{
					factors[i] = factors[i / k];
					break;
				}
			}
		}
	}

	std::cout << phi(87109) << std::endl;

	double min_r = (double) TARGET;
	int min_n = TARGET;

	for (int i = 4; i < TARGET; ++i)
	{
		int p = phi(i);
		double r = i / (double) p;

		if (r < min_r && perm(i, p))
		{
			min_r = r;
			min_n = i;
		}
	}

	std::cout << min_n << std::endl;
	return 0;
}
