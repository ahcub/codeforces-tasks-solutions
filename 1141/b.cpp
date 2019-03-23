#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main()
{
    unsigned int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    int max_length = 0;
    int currentLength = 0;
    for (int j = 0; j < 3; ++j) {
        for (int i = 0; i < n; ++i) {
            if (a[i] == 1) {
                currentLength++;
            } else {
                if (currentLength > max_length) {
                    max_length = currentLength;
                };
                currentLength = 0;
            }
        }
    }
    cout << max_length << endl;

}


