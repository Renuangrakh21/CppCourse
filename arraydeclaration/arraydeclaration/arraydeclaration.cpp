// arraydeclaration.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	char A[4] = { 'A',66,'C',68};

	for (char i = 0;i < 4; i++)
	{
		cout << A[i] << endl;
	}
	return 0;
}