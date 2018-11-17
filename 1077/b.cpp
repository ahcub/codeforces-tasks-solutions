#include <iostream>
#include <vector>

using namespace std;

int main()
{
    unsigned int n;
    cin >> n;
    vector<bool> a(n);
    for (int i = 0; i < n; ++i) {
        bool v;
        cin >> v;
        a[i] = v;
    }
    int k = 0;
    for (int i = 1; i < n; ++i) {
        if (a[i-1] && !a[i] && a[i+1]) {
            a[i+1] = false;
            k++;
        }
    }
    cout << k << endl;
}