// palindromeusingwhileloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, r, m, rev = 0;

	cout << "Enter a number: ";
	cin >> n;
	m = n;

	while (n > 0)
	{
		r = n % 10;
		n = n / 10;
		rev = rev * 10 + r;
	}
	if (rev == m)
		cout << "It is a Palindrome. ";
	else
		cout << "Not a Palindrome. ";

	return 0;
}