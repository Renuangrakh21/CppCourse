// reference.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int x = 10;
	int& y = x;

	cout << x << endl;

	y++;
	x++;

	cout << &x << " " << &y << endl;

	return 0;
}