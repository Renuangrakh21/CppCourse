// strtok.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<cstring>
using namespace std;

int main()
{
	char s1[20] = "x=10;y=20;z=35";

	char *token = strtok_s(s1,"=;");

	while (token != NULL)
	{
		cout << token << endl;
		token = strtok_s(NULL,"=;");
	}
	return 0;
}