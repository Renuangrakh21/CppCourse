// marrayusingforeachloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int A[2][3];

	for (auto& x : A)
	{
		for (auto& y : x)
		{
			cin >> y;
		}
		cout << endl;
	}

	for (auto& x : A)
	{
		for (auto& y : x)
		{
			cout << y << " ";
		}
		cout << endl;
	}
}