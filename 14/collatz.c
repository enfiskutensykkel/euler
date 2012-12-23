#include <stdio.h>
#include <inttypes.h>

uint64_t f(uint64_t n)
{
	uint64_t step = 0;

	while (n != 1) {
		++step;

		if (n % 2 == 0)
			n /= 2;
		else
			n = 3*n + 1;	
	}

	return step + 1;
}


uint64_t f_rec(uint64_t n)
{
	/* Turn on -foptimize-sibling-calls for tail-call elimination 
	 * (Not that it really matters in this case [recursion isn't too deep])
	 */
	if (n == 1)
		return 1;
	else if (n % 2 == 0)
		return 1 + f(n/2);
	else 
		return 1 + f(3*n + 1);
}


int main(void)
{
	uint64_t i, n, m, k;

  	for (i = 2, n = 0; i < 1000000; ++i) {
  		
		m = f_rec(i);

  		if (m > n) {
  			n = m;
  			k = i;
			printf("%llu:%llu\n", k, n);
  		}
  	}

	return 0;
}
