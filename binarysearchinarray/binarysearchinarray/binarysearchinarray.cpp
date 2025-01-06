// binarysearchinarray.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int A[10] = { 6,8,15,17,20,22,25,28,30,35 };
	int l = 0;
	int h = 9;
	int key = 0;
	int mid = 0;

	cout << "Enter key: ";
	cin >> key;

	while (l <= h)
	{
		mid = (l + h) / 2;
		if (key == A[mid])
		{
			cout << "Found out. " << mid;
			return 0;
		}
		else if (key < A[mid])
			h = mid - 1;
		else
			l = mid + 1;
	}
	cout << "Not Found. ";
}