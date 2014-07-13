#include <cstdio>
#include <set>
#include <list>
#include <vector>
#include <map>
#include <algorithm>

#define TARGET 6

using namespace std;

int P3(int n) { return (((n) * ((n) + 1)) >> 1); }
int P4(int n) { return ((n) * (n)); }
int P5(int n) { return (((n) * (3 * (n) - 1)) >> 1); }
int P6(int n) { return ((n) * (2 * (n) - 1)); }
int P7(int n) { return (((n) * (5 * (n) - 3)) >> 1); }
int P8(int n) { return ((n) * (3 * (n) - 2)); }

vector< vector<int> > numbers;


void generate(int (*f)(int))
{
	vector<int> results;

	for (int i = 1, n = 1; n <= 9999; n = f(++i))
	{
		if (n >= 1000)
		{
			results.push_back(n);
		}
	}

	numbers.push_back(results);
}

bool is_cyclic(int a, int b)
{
	return a % 100 == b / 100;
}

bool is_cyclic(vector<int>& chain)
{
	int i, n;
	for (i = 0, n = chain.size(); i < n - 1; ++i)
	{
		if (!is_cyclic(chain[i], chain[i + 1]))
		{
			return false;
		}
	}
	
	return true;
}

bool find_next(vector<int>& chain, char used)
{
	for (int i = 0, n = numbers.size(); i < n; ++i)
	{
		if (!(used & (1 << i)))
		{
			for (auto j = numbers[i].begin(); j != numbers[i].end(); ++j)
			{
				if (find(chain.begin(), chain.end(), *j) == chain.end())
				{
					chain.push_back(*j);
					if (is_cyclic(chain))
					{
						if (chain.size() == TARGET && is_cyclic(chain[TARGET-1], chain[0]))
						{
							return true;
						}

						if (find_next(chain, used | (1 << i)))
						{
							return true;
						}
					}
					chain.pop_back();
				}
			}
		}
	}

	return false;
}


int main()
{
	generate(&P3);
	generate(&P4);
	generate(&P5);
	generate(&P6);
	generate(&P7);
	generate(&P8);

	vector<int> chain;

	if (find_next(chain, 0))
	{
		int sum = 0;
		for (auto i = chain.begin(); i != chain.end(); ++i)
		{
			printf("%d\n", *i);
			sum += *i;
		}
		printf("sum: %d\n", sum);
	}

	return 0;
}
