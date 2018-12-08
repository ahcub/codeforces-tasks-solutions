#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
    unsigned int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            if ((i % j) == 0) {
                if ((i*j > n) && (i/j < n)) {
                    cout << i << " " << j << endl;
                    return 0;
                }
            }
        }
    }
    cout << -1 << endl;
}