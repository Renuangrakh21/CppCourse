// natureofroots.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<cmath>

using namespace std;

int main()
{
	int a, b, c, d, r1, r2;
	cout << "Enter a, b, c:";
	cin >> a >> b >> c;

	d = b * b - 4 * a * c;
	r1 = (-b + sqrt(d) / (2 * a));
	r2= (-b - sqrt(d) / (2 * a));

	if (d == 0)
	{
		cout << "Roots are real and equal." << endl;
		cout << (-b / (2 * a));
	}
	else if (d > 0)
	{
		cout << "Roots are real and unequal." << endl;
		cout << r1 << endl;
		cout << r2;
	}
	else
	{
		cout << "Roots are imaginary.";
	}
	return 0;
}