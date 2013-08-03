#include <stdio.h>

int fac(int n)
{
	int i, fac;

	if (n == 0) {
		return 1;
	}

	for (fac = 1, i = 1; i <= n; ++i) {
		fac *= i;
	}

	return fac;
}

int len(int n)
{
	int len;
	for (len = 0; n > 0; n /= 10, ++len);
	return len;
}

int sum(int n)
{
	int sum;

	for (sum = 0; n > 0; n /= 10) {
		sum += fac(n % 10);
	}

	return sum;
}

int main(void)
{
	int i, upper_lim, t_sum, w_sum;
	for (i = 1; len(fac(9) * i) > i; ++i);

	upper_lim = fac(9) * i;

	for (i = 3, w_sum = 0; i < upper_lim; ++i) {
		t_sum = sum(i);
		if (t_sum == i)
			w_sum += t_sum;
	}

	printf("%d\n", w_sum);
	return 0;
}
