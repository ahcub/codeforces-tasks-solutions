#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
    unsigned int n;
    cin >> n;
    vector<int> a(n);
    long int highest_el = 0;
    long int next_to_highest = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] > highest_el) {
            next_to_highest = highest_el;
            highest_el = a[i];
        } else if (a[i] > next_to_highest) {
            next_to_highest = a[i];
        }
    }
    long long int sum_of_elements = 0;
    for (auto& i : a)
        sum_of_elements += i;
    vector <int> p;
    for (int i = 0; i < n; ++i) {
        if (a[i] == highest_el) {
            if ((sum_of_elements - highest_el - next_to_highest) == next_to_highest) {
                p.push_back(i);
            }
        } else {
            if ((sum_of_elements - a[i] - highest_el) == highest_el) {
                p.push_back(i);
            }
        }
    }

    cout << p.size() << endl;
    for (auto& i : p)
        cout << i + 1 << " ";
    cout<<endl;
}