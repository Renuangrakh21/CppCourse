// strtolandstrtof.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	char s1[10] = "235";
	char s2[10] = "54.78";

	long int x = strtol(s1, NULL, 10);
	float y = strtof(s2, NULL);

	cout << x + 10 << endl << y - 5 << endl;

	return 0;
}