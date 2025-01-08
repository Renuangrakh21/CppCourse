// pointers.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int a = 10;
	int *p=&a;

	cout << a << endl;
	cout << &a << endl;
	cout << p << endl;
	cout << &p << endl;
	cout << *p << endl; // *p is for dereferencing.
}