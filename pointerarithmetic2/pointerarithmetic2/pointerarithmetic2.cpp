// pointerarithmetic2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int A[5] = { 2,4,6,8,10 };
	int* p = A;

	cout << *p << endl;
	cout << *(p + 2) << endl;

	return 0;
}