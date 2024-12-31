// discountedbillamount.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	float billamount;
	float discount = 0.0;

	cout << "Enter the bill amount: ";
	cin >> billamount;

	if (billamount >= 500)
		discount = billamount * 20 / 100;
	else if (billamount >= 100 && billamount < 500)
		discount = billamount * 10 / 100;

	cout << "Bill Amount is:" << billamount << endl;
	cout << "Discount is: " << discount << endl;
	cout << "Discounted ampunt is: " << billamount - discount << endl;

	return 0;
}