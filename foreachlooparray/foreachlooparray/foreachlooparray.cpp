// foreachlooparray.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int A[] = {2,3,6,4,9,7};

	for (int x : A)
	{
		cout << ++x << " ";
		cout << x << " ";
	}
	return 0;
}

