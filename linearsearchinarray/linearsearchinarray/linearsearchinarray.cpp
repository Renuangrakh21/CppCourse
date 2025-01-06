// linearsearchinarray.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int A[10];
	int n = 10;
	int key = 0;
	int i = 0;
	
	cout << "Enter number: ";
	
	for (int i = 0;i < 10;i++)
	{
		cin >> A[i];
	}
	cout << "Enter key: ";
	cin >> key;

	for (i = 0;i < n;i++)
	{
		if (key == A[i])
		{
			cout << "Found Out. "<< i;
			return 0;
		}
	}
	cout << "Not found. ";
}
