#include <iostream>
using namespace std;

// formal parameters
void rectangle(double w, double h, double& area, double& perimeter)
{
    area = w * h;
    perimeter = w + w + h + h;
}

int main()
{
    double area = 0;
    double perimeter = 0;

    //actual parameters
    rectangle(2, 3, area, perimeter);

    cout << area << " " << perimeter << endl;

    return 0;
}

//def rectangle(w, h):
//    area = w * h;
//    perimeter = w + w + h + h;
//    return area, perimeter
//
//rect_area, rect_peri = rectangle(2, 3);
//
//print rect_area, rect_peri  # print magically 6 10 with a space
