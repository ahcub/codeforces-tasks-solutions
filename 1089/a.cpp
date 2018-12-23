#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <string>

using namespace std;

int solve_for_three(int a, int b) {
    if ((a >= 75) && (b >= 0)){
        if ((a == 75) && (b <= 23)) {
            return 1;
        }
        if (((a - 75) <= (b - 23)) && ((a - 75) >= (b - 69))) {
            return 1;
        }
    }
    return 0;
}

int solve_two_sides(int (*func)(int, int), int a, int b) {
    int res = func(a, b);
    if (res) {
        return res;
    }
    res = -func(b, a);
    return res;
}

int solve_for_four(int a, int b) {
    if ((b >= 25) && (a >= 75)) {
        if ((a == 75) && (b >= 25) && (b <= 94)) {
            return 1;
        }
        if ((a > 75) && (a <= 98) && (b >= 25) && (b <= 94)) {
            return 1;
        }
        if (((b - 94) <= (a - 75)) && ((b - 94) >= (a - 167))) {
            return 1;
        }
        if (((b - 25) <= (a - 75)) && ((b - 25) >= (a - 98))) {
            return 1;
        }
    }
    return 0;
}

int solve_for_five(int a, int b) {
    if ((a >= 65) && (b >= 50)) {
        if ((a == 65) && (b >= 50) && (b <= 109)) {
            return 1;
        }
        if ((a > 65) && (a <= 111) && (b >= 50) && (b <= 109)) {
            return 1;
        }
        if (((b - 109) <= (a - 65)) && ((b - 109) >= (a - 111))) {
            return 1;
        }
        if (((b - 50) <= (a - 65)) && ((b - 50) >= (a - 111))) {
            return 1;
        }
    }
    return 0;
}

int define_winner(int a, int b) {
    int r3 = solve_two_sides(solve_for_three, a, b);
    int r4 = 2 * solve_two_sides(solve_for_four, a, b);
    int r5 = 3 * solve_two_sides(solve_for_five, a, b);
    if (r3 == 1) {
        return r3;
    }
    if (r4 == 2) {
        return r4;
    }
    if (r5 == 3) {
        return r5;
    }
    if (r5 == -3) {
        return -3;
    }
    if (r4 == -2) {
        return r4;
    }
    if (r3 == -1) {
        return r3;
    }
    return 0;
}

string generate_score_three(int a, int b, bool side) {
    int scores[3][2] = {{25, 0}, {25, 0}, {25, 0}};
    a = a - 75;
    scores[2][0] += a;
    if (scores[2][0] > 25) {
        scores[2][1] = scores[2][0] - 2;
        b = b - (scores[2][0] - 2);
    }
    if (b > 0) {
        if (b > 23) {
            scores[0][1] = 23;
            b = b - 23;
            if (b > 23) {
                scores[1][1] = 23;
                b = b - 23;
                scores[2][1] = b;
            } else {
                scores[1][1] = b;
            }
        } else {
            scores[0][1] = b;
        }
    }

    return to_string(scores[0][side])+":"+to_string(scores[0][!side]) + " " +
    to_string(scores[1][side])+":"+to_string(scores[1][!side]) + " " +
    to_string(scores[2][side])+":"+to_string(scores[2][!side]);
}

string generate_score_four(int a, int b, bool side) {
    int scores[4][2] = {{25, 0}, {25, 0}, {0, 25}, {25, 0}};
    a = a - 75;
    b = b - 25;
    if (a <= 23) {
        scores[2][0] += a;
        a = 0;
    } else {
        scores[2][0] += 23;
        a = a - 23;
    }
    if ((a + 25) <= (b - 2)) {
        scores[3][0] += a;
        if (scores[3][0] > 25) {
            scores[3][1] = scores[3][0] - 2;
            b = b - (scores[3][0] - 2);
        }
    } else {
        if ((b >= a) && (scores[2][0] == 23)) {
            scores[2][0] = scores[2][0] + a;
            scores[2][1] = scores[2][1] + a;
            b = b - a;
            a = 0;
        }
    }
    if (b > 0) {
        if (b > 23) {
            scores[0][1] = 23;
            b = b - 23;
            if (b > 23) {
                scores[1][1] = 23;
                b = b - 23;
                scores[3][1] = scores[3][1] + b;
                if (((scores[3][0] - scores[3][1]) <= 1) && scores[2][0] >= 1) {
                    int temp = scores[3][1] + 2 - scores[3][0];
                    scores[3][0] = scores[3][0] + temp;
                    scores[2][0] = scores[2][0] - temp;
                }
            } else {
                scores[1][1] = b;
            }
        } else {
            scores[0][1] = b;
        }
    }

    return to_string(scores[0][side])+":"+to_string(scores[0][!side]) + " " +
    to_string(scores[1][side])+":"+to_string(scores[1][!side]) + " " +
    to_string(scores[2][side])+":"+to_string(scores[2][!side]) + " " +
    to_string(scores[3][side])+":"+to_string(scores[3][!side]);
}

string generate_score_five(int a, int b, bool side) {
    int scores[5][2] = {{25, 0}, {25, 0}, {0, 25}, {0, 25}, {15, 0}};
    a = a - 65;
    b = b - 50;
    if (a <= 23) {
        scores[2][0] += a;
        a = 0;
    } else {
        scores[2][0] += 23;
        a = a - 23;
    }
    if (a <= 23) {
        scores[3][0] += a;
        a = 0;
    } else {
        scores[3][0] += 23;
        a = a - 23;
    }
    if ((a + 15) <= (b - 2)) {
        scores[4][0] += a;
        if (scores[4][0] > 15) {
            scores[4][1] = scores[4][0] - 2;
            b = b - (scores[4][0] - 2);
        }
    } else {
        if ((b >= a) && (scores[2][0] == 23)) {
            scores[2][0] = scores[2][0] + a;
            scores[2][1] = scores[2][1] + a;
            b = b - a;
            a = 0;
        }
    }
    if (b > 0) {
        if (b > 23) {
            scores[0][1] = 23;
            b = b - 23;
            if (b > 23) {
                scores[1][1] = 23;
                b = b - 23;
                scores[4][1] = scores[4][1] + b;
                if (((scores[4][0] - scores[4][1]) <= 1) && (scores[2][0] + scores[3][0]) >= 1) {
                    int temp = scores[4][1] + 2 - scores[4][0];
                    scores[4][0] = scores[4][0] + temp;
                    if (temp > scores[2][0]) {
                        int temp2 = temp + (scores[2][0] - temp);
                        scores[2][0] = scores[2][0] - temp2;
                        scores[3][0] = scores[3][0] - (temp-temp2);
                    } else {
                        scores[2][0] = scores[2][0] - temp;
                    }
                }
            } else {
                scores[1][1] = b;
            }
        } else {
            scores[0][1] = b;
        }
    }
    return to_string(scores[0][side])+":"+to_string(scores[0][!side]) + " " +
    to_string(scores[1][side])+":"+to_string(scores[1][!side]) + " " +
    to_string(scores[2][side])+":"+to_string(scores[2][!side]) + " " +
    to_string(scores[3][side])+":"+to_string(scores[3][!side]) + " " +
    to_string(scores[4][side])+":"+to_string(scores[4][!side]);
}

int main()
{
    unsigned int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first;
        cin >> a[i].second;
    }
    for (int i = 0; i < n; ++i) {
        if ((a[i].first < 65 && a[i].second < 65)) {
            cout << "Impossible" << endl;
        } else {
            int winner = define_winner(a[i].first, a[i].second);
            if (winner == 0) {
                cout << "Impossible" << endl;
            } else {
                if (winner == 1) {
                    cout << "3:0" << endl;
                    cout << generate_score_three(a[i].first, a[i].second, false) << endl;
                }
                if (winner == 2) {
                    cout << "3:1" << endl;
                    cout << generate_score_four(a[i].first, a[i].second, false) << endl;
                }
                if (winner == 3) {
                    cout << "3:2" << endl;
                    cout << generate_score_five(a[i].first, a[i].second, false) << endl;
                }
                if (winner == -3) {
                    cout << "2:3" << endl;
                    cout << generate_score_five(a[i].second, a[i].first, true) << endl;
                }
                if (winner == -2) {
                    cout << "1:3" << endl;
                    cout << generate_score_four(a[i].second, a[i].first, true) << endl;
                }
                if (winner == -1) {
                    cout << "0:3" << endl;
                    cout << generate_score_three(a[i].second, a[i].first, true) << endl;
                }
            }
        }
    }
}
