// condstatementMaxof2numbers.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int x, y;
	cout << "Enter two numbers: ";
	cin >> x >> y;
	if (x > y)
	{
		cout << "Maximum number is: " << x;
	}
	else
	{
		cout << "Maximum number is: " << y;
	}
	return 0;
}