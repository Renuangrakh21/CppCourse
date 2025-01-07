// factorialusingforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, i, fact = 1;

	cout << "Enter a number: ";
	cin >> n;

	for (i = 1;i <= n;i++)
	{
		fact *= i;
	}
	cout << "Factorial of " << n << " is " << fact;

	return 0;
}