// factorsofnusingforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, i;

	cout << "Enter a number: ";
	cin >> n;

	for (i = 1;i <= n; i++)
	{
		if (n % i == 0)
		{
			cout << "Factor of " << n << " is " << i << endl;
		}
	}
	return 0;
}