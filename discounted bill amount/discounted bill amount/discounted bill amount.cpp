// discounted bill amount.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int actual_amount;
	float discounted_amount;

	cout << "Enter the amount: ";
	cin >> actual_amount;

	if (actual_amount >= 5000)
	{
		discounted_amount = actual_amount - actual_amount * 20 / 100.0;
		cout << "The bill before discount = " << actual_amount << endl;
		cout << "Discounted Bill = " << discounted_amount;
	}
	else if (actual_amount >= 2000 && actual_amount < 5000)
	{
		discounted_amount = actual_amount - actual_amount * 10 / 100.0;
		cout << "The bill before discount = " << actual_amount << endl;
		cout << "Discounted Bill = " << discounted_amount;

	}
	else
	{
		discounted_amount = actual_amount - actual_amount * 5 / 100.0;
		cout << "The bill before discount = " << actual_amount << endl;
		cout << "Discounted Bill = " << discounted_amount;
	}
	return 0;
}