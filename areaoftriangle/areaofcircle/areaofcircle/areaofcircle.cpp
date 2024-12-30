// areaofcircle.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include<iostream>

using namespace std;

int main()
{
	float r, area;
	cout << "Enter radius: ";
	cin >> r;
	area = 3.1425f * r * r;
	cout << "Area is: " << area;
	return 0;
}