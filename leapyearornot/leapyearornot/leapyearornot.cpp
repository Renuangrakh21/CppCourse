// leapyearornot.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int year;
	cout << "Enter a year:";
	cin >> year;

	if (year % 4 == 0)
	{
		cout << "It is a leap year.";
	}
	else if (year % 100 == 0)
	{
		cout << "It is a leap year.";
	}
	else if (year % 400 == 0)
	{
		cout << "It is a leap year.";
	}
	else
	{
		cout << "Not a leap year.";
	}
	return 0;
}