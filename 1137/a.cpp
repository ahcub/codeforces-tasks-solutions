#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main()
{
    unsigned int n, m;
    cin >> n >> m;
    vector<vector<unsigned int>> a(n, vector<unsigned int>(m));
    for (unsigned int i = 0; i < n; i++) {
        for (unsigned int j = 0; j < m; j++)
            cin >> a[i][j];
    }
    int vc = 0;
    int hc = 0;
    vector<vector<unsigned int>> verticals(m);
    vector<vector<unsigned int>> horizontals(n);
    vector<map<int, int>> vp_maps(m);
    vector<map<int, int>> hp_maps(n);
    vector<vector<unsigned int>> res(n, vector<unsigned int>(m));
    for (unsigned int i = 0; i < n; i++) {
        for (unsigned int j = 0; j < m; j++) {
            vector<unsigned int> v;
            if (j >= vc) {
                vector<unsigned int> v(n);
                for (unsigned int k = 0; k < n; ++k) {
                    v[k] = a[k][j];
                }
                sort(v.begin(), v.end());
                v.erase(unique(v.begin(), v.end()), v.end());
                verticals[j] = v;
                for (int t = 0; t < v.size(); ++t)
                    vp_maps[j][v[t]] = t;
                vc++;
            }
            v = verticals[j];
            vector<unsigned int> h;
            if (i >= hc){
                vector<unsigned int> h(m);
                for (unsigned int k = 0; k < m; ++k) {
                    h[k] = a[i][k];
                }
                sort(h.begin(), h.end());
                h.erase(unique(h.begin(), h.end()), h.end());
                horizontals[i] = h;
                for (int t = 0; t < h.size(); ++t)
                    hp_maps[i][h[t]] = t;
                hc++;
            }
            h = horizontals[i];

            unsigned int vp = vp_maps[j][a[i][j]];
            unsigned int hp = hp_maps[i][a[i][j]];
            if (hp+1 != h.size() || vp+1 != v.size())
                res[i][j] = max(v.size(), h.size()) + max(hp, vp) - min(hp, vp);
            else
                res[i][j] = max(v.size(), h.size());
        }
    }
    for (unsigned int i = 0; i < n; i++) {
        for (unsigned int j = 0; j < m; j++)
            cout << res[i][j] << ' ';
        cout << endl;
    }
}


