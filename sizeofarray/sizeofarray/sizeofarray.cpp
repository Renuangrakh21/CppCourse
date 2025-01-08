// sizeofarray.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int size;
	cout << "Enter the number of elements: ";
	cin >> size;

	int A[size];

	cout << sizeof A << endl;

	return 0;
}