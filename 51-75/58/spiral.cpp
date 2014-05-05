#include <cstdio>
#include <cmath>

inline bool is_prime(int n)
{
	for (int i = 2; i <= sqrt(n) + 1; ++i)
	{
		if (n % i == 0)
			return false;
	}

	return true;
}

inline int power(int a, int n)
{
	int b = a;
	while (--n) b *= a;
	return b;
}

inline int calculate_side(const int n)
{
	if (n < 1 || n % 2 == 0)
		return 0;

	const int m = power(n, 2);
	int primes = 0;

	for (int i = power(n - 2, 2) + 1, j = 1; i <= m; ++i, j = (j + 1) % (n - 1))
	{
		if (j % n == 0 && is_prime(i))
		{
			++primes;
		}
	}

	return primes;
}

int main()
{
	int primes = 0;
	int corners = 1;
	int side_length;
	for (side_length = 3; ; side_length += 2)
	{
		corners += 4;
		primes += calculate_side(side_length);

		if (primes / (double) corners < .1)
			break;
	}

	printf("%d\n", side_length);

	return 0;
}
