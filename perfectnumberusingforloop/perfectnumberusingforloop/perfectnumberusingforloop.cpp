// perfectnumberusingforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, i, sum = 0;

	cout << "Enter a number: ";
	cin >> n;

	for (i = 1;i <= n;i++)
	{
		if (n % i == 0)
		{
			sum += i;
		}
	}
	if (2 * n == sum)
		cout <<sum<<" Perfect number. ";
	else
		cout <<sum<<" Not a perfect number. ";

	

	return 0;
	} 