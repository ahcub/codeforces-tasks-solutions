#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    unsigned int n, k;
    cin >> n >> k;
    vector<unsigned int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    std::sort(a.begin(), a.end());
    unsigned int latest = a[0];
    unsigned int values_printed = 0;
    if (latest != 0) {
        cout << latest << endl;
        values_printed++;
        if (values_printed >= k) {
            return 0;
        }
    }

    for (int j = 1; j < n; ++j) {
        if (latest < a[j]){
            cout << a[j] - latest << endl;
            values_printed++;
            latest = a[j];
            if (values_printed >= k) {
                return 0;
            }
        }
    }
    for (int l = 0; l < k - values_printed; ++l) {
        cout << 0 << endl;
    }
}