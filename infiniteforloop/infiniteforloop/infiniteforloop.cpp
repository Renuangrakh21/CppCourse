// infiniteforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int i = 0;

	for (;;)
	{
		cout << i << " Hello\n";
		i++;
		if (i > 10)
			break;
	}
	return 0;
}