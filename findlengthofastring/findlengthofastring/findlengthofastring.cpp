// findlengthofastring.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include<iostream>
#include<string>

using namespace std;

int main()
{   //method 1:

	string str = "WELCOME";

	int count = 0;
	
	for (int i = 0;str[i] != '\0';i++)
	{
		count++;
	}
	cout << "Length is " << count << endl;

	//method 2:

	string str1 = "TODAY";

	string::iterator it;
	
	for (it = str1.begin();it != str1.end();it++)
	{
		count++;
	}
	cout << "Length is " << count << endl;
	return 0;
}