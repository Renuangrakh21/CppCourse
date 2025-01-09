// stringdemo.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	char x = 'A';

	char S[10] = "Hello";

	char A[] = "Hello";

	char B[] = { 'H','e','l','l','o','\0' };

	char C[] = {65,66,67,68,'\0'};

	cout << x << endl;
	cout << S << endl;
	cout << A << endl;
	cout << B << endl;
	cout << C << endl;

	// char *S = "Hello"; not supported by cpp 11 compiler

	return 0;
}