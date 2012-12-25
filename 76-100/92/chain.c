#include <stdio.h>
#include <stdint.h>

#define N 10000000

char found[N/8] = {0};
char result[N/8] = {0};

int chain(uint64_t x)
{
	uint64_t y, z;

	if (found[x/8] & (1 << (x%8)))
		return result[x/8] & (1 << (x%8));

	y = 0; z = x;
	while (z) {
		y += (z % 10) * (z % 10);
		z /= 10;
	}

	z = chain(y);
	found[x/8] |= (1 << (x%8));
	if (z)
		result[x/8] |= (1 << (x%8));

	return z;
}

int main(void)
{
	uint64_t i, k;
	found[1 / 8] |= 1 << 1;
	found[89 / 8] |= 1 << (89 % 8);
	result[89 / 8] |= 1 << (89 % 8);

	for (i = 1, k = 0; i < N; ++i)
		if (chain(i))
			k += 1;

	printf("%llu\n", k);

	return 0;
}
