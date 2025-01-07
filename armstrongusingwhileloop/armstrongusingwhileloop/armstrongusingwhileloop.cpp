// armstrongusingwhileloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, r, sum = 0, m;

	cout << "Enter a number: ";
	cin >> n;
	m = n;

	while (n > 0)
	{
		r = n % 10;
		n = n / 10;
		sum = sum + r * r * r;
	}
	if (sum == m)
		cout << "It is a armstrong number. ";
	else
		cout << "Not a armstrong number. ";

	return 0;
}