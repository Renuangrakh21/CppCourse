// strcmp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	char s1[20] = "Hello";
	char s2[20] = "Hello";

	cout << strcmp(s1, s2) << endl;

	char s3[20] = "hello";
	char s4[20] = "Hello";

	cout << strcmp(s3, s4) << endl;

	char s5[20] = "Hello";
	char s6[20] = "hello";

	cout << strcmp(s5, s6) << endl;

	char s7[20] = "minor";
	char s8[20] = "elder";

	cout << strcmp(s7, s8) << endl;

	return 0;
}