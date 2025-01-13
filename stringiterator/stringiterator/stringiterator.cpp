// stringiterator.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include<iostream>
#include<string>

using namespace std;

int main()
{
	string str = "today";

	string::iterator it;

	for (it = str.begin();it != str.end();it++)
	{
		cout << *it ;
		*it = *it - 32;
	}

	cout << str << endl;

	string s1 = "Programming";

	string::reverse_iterator iter;

	for (iter = str.rbegin();iter != str.rend();iter++)
	{
		cout << *iter;
	}
	
	return 0;
}