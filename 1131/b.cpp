#include <iostream>
#include <algorithm>


using namespace std;

int main()
{
    unsigned int n, draw_counter, x, y, prev_x, prev_y;
    cin >> n;
    draw_counter = 1;
    prev_x = 0;
    prev_y = 0;
    for (int i = 0; i < n; ++i) {
        cin >> x >> y;
        if (!((prev_x == x) && ((prev_y == y)))) {
            if ((prev_x < prev_y) && (x >= y)) {
                draw_counter = draw_counter + (y - prev_y) + 1;
            } else if ((prev_x > prev_y) && (x <= y)) {
                draw_counter = draw_counter + (x - prev_x) + 1;
            } else if ((prev_x < prev_y) && (x >= prev_y)) {
                draw_counter = draw_counter + (x - prev_y) + 1;
            } else if ((prev_y < prev_x) && (y >= prev_x)) {
                draw_counter = draw_counter + (y - prev_x) + 1;
            } else if ((prev_x == prev_y) && (x != y)) {
                draw_counter = draw_counter + min(x - prev_x, y - prev_y);
            } else if ((prev_x == prev_y) && (x == y)) {
                draw_counter = draw_counter + (x - prev_x);
            }
        }
        prev_x = x;
        prev_y = y;
    }
    cout << draw_counter << endl;
}
