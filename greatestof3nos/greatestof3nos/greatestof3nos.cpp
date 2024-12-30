// greatestof3nos.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int a, b, c;
	cout << "Enter 3 numbers: ";
	cin >> a >> b >> c;

	if (a > b && a >> c)
	{
		cout << a<<" is greatest number." ;
	}
	else if (b > c)
	{
		cout << b << " is greatest number.";
	}
		else
	{
		cout << c << " is greatest number.";
	}
	
	return 0;
}