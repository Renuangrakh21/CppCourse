// youngornot.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int age;
	cout << "Enter age: ";
	cin >> age;

	if (age >= 12 && age <= 50)
	{
		cout << "young";
	}
	else
	{
		cout << "not young";
	}
	return 0;
}