// strcat.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<cstring>

using namespace std;

int main()
{
	char s1[20] = "Good";
	char s2[20] = " Morning";

	char s3[20] = "Good";
	char s4[20] = " Morning";

	strcat_s(s1, s2);
	strncat_s(s3, s4, 3);

	cout << s1 << endl;
	cout << s3 << endl;

	return 0;
}