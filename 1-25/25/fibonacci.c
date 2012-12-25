#include <math.h>
#include <stdio.h>

int main(void)
{
	int n, i;
	long double lim = powl(10, 999);
	long double F[] = {0.0, 1.0, 0.0};
	i = 1; n = 1;

	while (F[i] < lim) {
		i = (i + 1) % 3;
		F[i] = F[(i+1) % 3] + F[(i+2) % 3];
		++n;
	}

	printf("%d\n", n);
	return 0;
}
