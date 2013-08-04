#include <cstdio>
#include <map>
#include <vector>
#include <tr1/cstdint>

using std::map;
using std::pair;
using std::vector;


static map<uint64_t,bool> eventual;


uint64_t reverse(uint64_t number)
{
	uint64_t reverse;

	// Reverse number
	for (reverse = 0; number > 0; number /= 10)
	{
		reverse *= 10;
		reverse += number % 10;
	}

	return reverse;
}


bool palindromic(uint64_t number, int level=50)
{
	// Check if we have registered this number already
	map<uint64_t,bool>::iterator found = eventual.find(number);
	if (found != eventual.end())
	{
		if (level == 50)
		{
			return palindromic(number + reverse(number), --level);
		}
		return found->second;
	}

	// Give up after 50 steps
	if (level < 0)
	{
		eventual.insert(pair<uint64_t,bool>(number, false));
		return false; 
	}

	// Check if number is an actual palindrome 
	if (reverse(number) == number)
	{
		eventual.insert(pair<uint64_t,bool>(number, true));
		if (level == 50)
		{
			return palindromic(number + reverse(number), --level);
		}
		return true;
	}

	// Reverse number and add and check if that eventually becomes palindromic
	bool eventually = palindromic(number + reverse(number), --level);
	eventual.insert(pair<uint64_t,bool>(number, eventually));
	return eventually;
}


int main(void)
{
	vector<uint64_t> lychrel;
	const uint64_t limit = 10000;

	for (uint64_t i = 10; i < limit; ++i)
	{
		if (!palindromic(i))
		{
			lychrel.push_back(i);
		}
	}

	printf("Lychrel numbers below %llu: %u\n", limit, lychrel.size());

	return 0;
}
