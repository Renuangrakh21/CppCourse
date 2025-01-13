// changecasesofletters.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include<iostream>
using namespace std;

int main()
{
	string str = "WeLcOMe";

	for (int i = 0;str[i] != '\0';i++)
	{
		if (str[i] >= 65 && str[i] <= 90)
		{
			str[i] = str[i] + 32;
		}
	}
	cout << str << endl;

	return 0;

}