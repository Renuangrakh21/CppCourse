// pointerarithmetic3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int A[5] = { 2,4,6,8,10 };
	int* p = A;

	for (int i = 0;i < 5;i++)
	{
		cout << A[i] << endl;
	}
	return 0;
}