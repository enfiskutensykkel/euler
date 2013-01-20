#include <stdio.h>

#define TARGET_CHANGE 200

static int table[TARGET_CHANGE+1] = {0};

static int coins[] = {1, 2, 5, 10, 20, 50, 100, 200};

int main(void)
{
	int i, j;

	table[0] = 1;

	for (i = 0; i < sizeof(coins)/sizeof(int); ++i)
		for (j = coins[i]; j <= sizeof(table)/sizeof(int); ++j)
			table[j] += table[j - coins[i]];

	printf("%d\n", table[TARGET_CHANGE]);

	return 0;
}
