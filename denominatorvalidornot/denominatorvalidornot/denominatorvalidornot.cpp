// denominatorvalidornot.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int a, b, c;
	cout << "Enter two number: ";
	cin >> a >> b;
	if (b == 0)
	{
		cout << "Division by zero. ";
	}
	else
	{
		c = a / b;
		cout << "Solution is: " << c;
	}
	return 0;
}