#include <stdio.h>

double factorial(double n, double r)
{
	if (n <= 1)
		return r;

	return factorial(n - 1, n * r);
}

inline double fac(double n)
{
	return factorial(n, 1);
}

double nCr(long n, long r)
{
	return (fac(n) / (fac(r) * fac(n - r)));
}

int main(void)
{
	long n, r, count = 0;

	for (n = 1; n <= 100; ++n)
	{
		for (r = 1; r <= n; ++r)
		{
			if (nCr(n, r) > 1000000)
			{
				++count;
			}
		}
	}

	printf("%ld\n", count);
	return 0;
}
