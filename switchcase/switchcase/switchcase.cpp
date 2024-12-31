// switchcase.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int day;
	cout << "Enter day no. :";
	cin >> day;

	switch (day)
	{
	case 1: cout << "Mon";
		break;
	case 2: cout << "Tue";
		break;
	case 3: cout << "Wed";
		break;
	case 4: cout << "Thu";
		break;
	case 5: cout << "Fri";
		break;
	case 6: cout << "Sat";
		break;
	case 7: cout << "Fri";
		break;
	default: cout << "Invalid Day.";
	}
	return 0;
}