// nestedforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	for (int i = 1;i <= 3;i++)
	{
		for (int j = 1;j <= 3;j++)
		{
			cout << "(" << i << "," << j << ")";
		}
		cout << endl;
	}
	return 0;
}