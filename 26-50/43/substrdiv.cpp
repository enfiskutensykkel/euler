#include <cstdint>
#include <cstdio>
#include <vector>

inline uint64_t factorial(uint32_t n, uint64_t result = 1)
{
	if (n <= 1)
		return result;

	return factorial(n - 1, n * result);
}

inline bool divisible(uint32_t* digits)
{
	uint32_t divisors[] = {1, 2, 3, 5, 7, 11, 13, 17};
	for (uint32_t i = 1; i < 8; ++i) {
		uint32_t dividend = 100 * digits[i] + 10 * digits[i + 1] + digits[i + 2];

		if (dividend % divisors[i] != 0)
			return false;
	}

	return true;
}

inline void swap(uint32_t& a, uint32_t& b)
{
	uint32_t t = a;
	a = b;
	b = t;
}

int main()
{
	uint32_t permutation[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	uint64_t lim = 9 * factorial(9);
	uint64_t res = 0;

	while (--lim > 0) {
		uint32_t i, j;
		
		for (i = 9; permutation[i - 1] >= permutation[i]; --i);
		for (j = 10; permutation[j - 1] <= permutation[i - 1]; --j);
		swap(permutation[i - 1], permutation[j - 1]);

		j = 10;
		++i;
		while (i < j) {
			swap(permutation[i - 1], permutation[j - 1]);
			i++;
			j--;
		}

		if (divisible(permutation)) {
			uint64_t num = 0;
			for (i = 0; i < 10; ++i)
				num = 10 * num + permutation[i];
			printf("%lu\n", num);
			res += num;
		}
	}

	printf("%lu\n", res);
	return 0;
}
