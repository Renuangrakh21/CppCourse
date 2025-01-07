// reverseanumberusingwhileloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int r, n, rev = 0;

	cout << "Enter a number: ";
	cin >> n;

	while (n > 0)
	{
		r = n % 10;
		n = n / 10;
		rev = rev * 10 + r;
	}
	cout << "Reverse number is " << rev;

	return 0;
}