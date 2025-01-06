// sumofNusingforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, i, sum = 0;

	cout << "Enter number: ";
	cin >> n;

	for (i = 1;i <= n;i++)
	{
		sum += i;
	}
	cout << "Sum of first N numbers is: " << sum;
	return 0;
}