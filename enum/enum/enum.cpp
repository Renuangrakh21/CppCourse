// enum.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

enum day { mon=1,tue,wed,thu=8,fri,sat,sun=15};
enum dept { cs, it, mech, elec};

int main()
{
	day d;
	dept dep;

	d = tue;
	dep = mech;

	cout << mon << endl;
	cout << tue << endl;
	cout << wed << endl;
	cout << thu << endl;
	cout << fri << endl;
	cout << sat << endl;
	cout << sun << endl;

	cout << cs << endl;
	cout << it << endl;
	cout << mech << endl;
	cout << elec << endl;

	return 0;
	

}