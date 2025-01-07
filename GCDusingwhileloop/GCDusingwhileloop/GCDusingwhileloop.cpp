// GCDusingwhileloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, m;

	cout << "Enter two numbers: ";
	cin >> n >> m;

	while (m != n)
	{
		if (m > n)
			m = m - n;
		else if (n > m)
			n = n - m;
	}
	cout << m;
}