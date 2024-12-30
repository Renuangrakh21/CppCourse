// netsalary.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	float BasicSalary;
	float PercentAllowance;
	float PercentDeduction;
	float NetSalary;

	cout << "Enter the Basic Salary: ";
	cin >> BasicSalary;
	cout << "Enter the Percentage of Allowance: ";
	cin >> PercentAllowance;
	cout << "Enter the Percentage of Deduction: ";
	cin >> PercentDeduction;

	NetSalary = BasicSalary + BasicSalary * PercentAllowance / 100 - BasicSalary * PercentDeduction/100;

	cout << "Net Salary: " << NetSalary;

	return 0;

}

	