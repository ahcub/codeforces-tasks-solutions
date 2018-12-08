#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    unsigned int n;
    cin >> n;
    vector<unsigned int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int sum = 0;
    cout << n+1 << endl;
    for (int j = n-1; j >= 0; j--) {
        int add=(j-(a[j]+sum)%n+n)%n;
        cout << "1 " << j + 1 << " " << add << endl;
        sum += add;
    }
    cout << "2 " << n << " " << n << endl;
}