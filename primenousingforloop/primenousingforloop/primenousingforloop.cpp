// primenousingforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, i, count = 0;

	cout << "Enter a number: ";
	cin >> n;

	for (i = 1;i <= n;i++)
	{
		if (n % i == 0)
		{
			count++;
		}
	}
	if (count == 2)
		cout << "It is a prime number. ";
	else
		cout << "Not a prime number. ";

	return 0;
}