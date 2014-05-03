#include <stdio.h>
#include <inttypes.h>

int64_t factorial(int64_t n, int64_t a)
{
	if (n <= 1)
		return a;

	/* tail call (so that the compiler can do some magic) */
	return factorial(n-1, a*n);
}


int main(void)
{
	int tbl[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	int64_t num, idx, fac, lim, i, j;

	num = 0; lim = 1000000L - 1; /* target is the millionth permutation */
	for (i = 1; lim > 0 && i < 10; ++i) {
		fac = factorial(10 - i, 1);

		idx = lim / fac;
		lim = lim % fac;

		num = 10 * num + tbl[idx];
		for (j = idx; j < 9; ++j)
			tbl[j] = tbl[j+1];
		tbl[j] = -1;
	}
	
	for (i = 0; tbl[i] != -1 && i < 10; ++i)
		num = 10 * num + tbl[i];

	//printf("%lld\n", num);
	printf("%ld\n", num);
	return 0;
}
