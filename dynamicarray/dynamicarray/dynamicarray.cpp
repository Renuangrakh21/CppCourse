// dynamicarray.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int* p = new int[20];

	cout << p<<endl;

	delete []p;

	p = new int[40];

	cout << p;

	return 0;
}