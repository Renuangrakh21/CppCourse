// readandwritestring.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	char s[20];
	char a[50];

	cout << "Enter you name: " ;
	cin.get(s, 50);

	cout << "Welcome " << s << endl;

	cin.ignore();

	cout << "Enter you name: ";
	cin.get(a,50);

	cout <<"Welcome "<< a << endl;

return 0;
}