// strchr.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<cstring>

using namespace std;

int main()
{
	char s1[20] = { "Programming" };
	char s2[20] = { "Programming" };

	cout << strchr(s1, 'r') << endl;
	cout << strrchr(s2, 'r') << endl;

	return 0;
}
