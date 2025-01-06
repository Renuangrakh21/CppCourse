// accessingmaaray.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int A[2][3] = {{2,4,6},{7,6,5}};

	for (int i = 0;i < 2;i++)
	{
		for (int j = 0;j < 3;j++)
		{
			cout << A[i][j]<<" ";
		}
		cout << endl;
	}


}