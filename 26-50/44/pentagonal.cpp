#include <cstdio>
#include <cmath>


int P(int n)
{
	return n * (3*n - 1) / 2;
}



bool P_inv(int x)
{
	// Pentagonal check found on wikipedia
	double n = (sqrt(24*x + 1) + 1.0) / 6.0;
	return n == floor(n);
}



int main(void)
{
	int k, j, D;
	int n, m;

	for (k = 1; ; ++k)
	{
		n = P(k);

		for (j = k-1; j > 0; --j)
		{
			m = P(j);
			if (P_inv(n - m) && P_inv(n + m))
				goto found;
		}
	}

found:
	printf("%d %d, D=%d\n", k, j, n-m);
	return 0;
}
