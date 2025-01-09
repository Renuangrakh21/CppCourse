// strcpy.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	char s1[20] = "Good";
	char s2[20] = "";

	strcpy_s(s2, s1);

	cout << s2 << endl;

	char s3[20] = "Good";
	char s4[20] = "";

	strncpy_s(s4, s3, 2);

	cout << s4 << endl;

	return 0;
}