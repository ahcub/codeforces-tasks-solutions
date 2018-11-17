#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        long long int a, b, k;
        cin >> a >> b >> k;
        cout << (a * (k / 2)) - (b * (k / 2)) + (a * (k % 2)) << endl;
    }
}