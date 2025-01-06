// 1tonusingdowhileloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, i = 1;

	cout << "Enter number: ";
	cin >> n;

	do
	{
		cout << i << endl;
		i++;
	} while (i <= n);
	return 0;
}