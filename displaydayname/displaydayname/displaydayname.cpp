// displaydayname.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int day;
	cout << "Enter a day: ";
	cin >> day;

	if (day == 1)
	{
		cout << "sun" << endl;
	}
	else if (day == 2)
	{
		cout << "mon" << endl;
	}
	else if (day == 3)
	{
		cout << "tue" << endl;
	}
	else if (day == 4)
	{
		cout << "wed" << endl;
	}
	else if (day == 5)
	{
		cout << "thu" << endl;
	}
	else if (day == 6)
	{
		cout << "fri" << endl;
	}
	else if (day == 7)
	{
		cout << "sat" << endl;
	}


}