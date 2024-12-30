// rollnovalidornot.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int roll;
	cout << "Enter roll number: ";
	cin >> roll;
	if (roll < 1)
	{
		cout << "Roll number is invalid.";
	}
	else {
		cout << "Roll number is valid.";
		
	}
	return 0;
}