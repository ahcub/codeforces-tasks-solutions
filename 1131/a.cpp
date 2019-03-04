#include <iostream>

using namespace std;

int main()
{
    unsigned int w1, h1, w2, h2;
    cin >> w1 >> h1 >> w2 >> h2;

    cout << (((w1*2) + (h1*2)) + 6) + (h2 - 1)*2 << endl;

}
