#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void sieve(int len, char *map)
{
	int i, j, n, m;

	/* Boundaries */
	n = len; m = (int) sqrt(n);

	/* Initialize bitmap */
	for (i = 0; i < n / 8; ++i)
		map[i] = 0xff;

	/* Do sieve of Eratosthenes */
	for (i = 2; i < m; ++i)
		if (map[i / 8] & (1 << (i % 8)))
			for (j = i << 1; j < n; j += i)
				map[j / 8] &= ~(1 << (j % 8));
}



int main(void)
{
	char *bitmap;
	int i, j;

	bitmap = malloc(0xffffff);

	sieve(0xffffff, bitmap);
	for (i = 2, j = 0; j < 10001; ++i)
		if (bitmap[i / 8] & (1 << (i % 8)))
			++j;
	printf("%d\n", i-1);

	free(bitmap);
	return 0;
}
