// multiplicationtableusingforloop.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int n, i;
	
	cout << "Enter number: ";
	cin >> n;

	for (i = 1;i <= 10;i++)
	{
		cout << n << " X " << i << " = " << n * i;
		cout << endl;
	}
	return 0;
}