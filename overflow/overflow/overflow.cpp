// overflow.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
int main()
{
	char a = 128;
	cout << (int)a << endl;
	char b = 127;
	b++;
	cout << (int)b << endl;
	char c = -129;
	cout << (int)c << endl;
	char d = -128;
	d--;
	cout << (int)d << endl;
	int e = INT_MAX;
	e++;
	cout << (int)e << endl;
	return 0;
}