// stringfunctions.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	char s[20] = "Hello World";
	char *a;

	cout << strlen(s) << endl;

	cout << "Enter a string: ";
	cin >> a;

	cout << "Length: " << strlen(a) << endl;

	return 0;
}