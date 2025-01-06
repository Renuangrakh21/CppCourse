// drawingpattern1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int count = 1;

	for (int i = 0;i < 4;i++)
	{
		for (int j = 0;j < 4;j++)
		{
			cout << count << " ";
			count++;
		}
		cout << endl;
	}
	return 0;
}