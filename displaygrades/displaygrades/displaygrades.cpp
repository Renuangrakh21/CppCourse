// displaygrades.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

int main()
{
	int m1, m2, m3, Total;
	float Avg;

	cout << "Enter marks of three subjects:";
	cin >> m1 >> m2 >> m3;

	Total = m1 + m2 + m3;
	Avg = Total / 3.0;

	if (Avg >= 60)
	{
		cout << "Grade A" << endl;
		cout << "Total is: " << Total << endl;
		cout << "Average is: " << Avg << endl;
	}
	else if (Avg>=35 && Avg < 60)
	{
		cout << "Grade B" << endl;
		cout << "Total is: " << Total << endl;
		cout << "Average is: " << Avg << endl;
	}
	else
	{
		cout << "Grade C" << endl;
		cout << "Total is: " << Total << endl;
		cout << "Average is: " << Avg << endl;

	}

	return 0;

		
}