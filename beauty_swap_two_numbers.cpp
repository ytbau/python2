#include <iostream>
using namespace std;

int main()
{
    int a = 66;
    int b = 99;
    cout << a << " " << b << endl;
    swap(a, b); //English-like line
    cout << a << " " << b << endl;

    return 0;
}

//a = 66
//
//b = 99
//
//print a, b # print 66 99
//
//a, b = b, a
//
//print a, b # print 99 66
