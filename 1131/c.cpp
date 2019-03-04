#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    unsigned int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    for (int i = 0; i < n; i+=2) {
        cout << a[i] << ' ';
    }
    if ((n % 2) == 0){
        for (int i = n-1; i > 0; i-=2) {
            cout << a[i] << ' ';
        }
    } else {
        for (int i = n-2; i > 0; i-=2) {
            cout << a[i] << ' ';
        }
    }
}
