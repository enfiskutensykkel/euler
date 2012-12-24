#include <stdio.h>
#include <math.h>

#define N 1000.0

/* Not efficient, but we can bruteforce this 
 * You need to multiply the three factors manually, 
 * since it overflows with printf.
 */
int main(void)
{
	double a, b, c;

	for (a = 0.0; a < N; ++a)
		for (b = a+1.0; b < N; ++b)
			if (a + b + sqrt(pow(a,2) + pow(b,2)) == 1000) 
				printf("%g %g %g\n", a, b, 1000-a-b);

	return 0;
}
