#include <iostream>
#include <vector>

using namespace std;

int sandCnt, xmax, ymax;
vector<vector<char>> grid;

void simulate() {
    while (true) {
        int x = 500;
        int y = 0;
        while (true) {
            // cout << x << " " << y << endl;
            if (grid[y + 1][x] == '.') {
                y++;
            } else if (grid[y + 1][x - 1] == '.') {
                x--;
                y++;
            } else if (grid[y + 1][x + 1] == '.') {
                x++;
                y++;
            } else {
                grid[y][x] = 'O';
                if (x == 500 && y == 0) {
                    sandCnt++;
                    return;
                }
                break;
            }
        }
        sandCnt++;
    }
}

void draw(int x1, int y1, int x2, int y2) {
    // cout << "Line: " << endl;
    for (int i = min(x1, x2); i <= max(x1, x2); i++) {
        for (int j = min(y1, y2); j <= max(y1, y2); j++) {
            grid[j][i] = '#';
            // cout << j << " " << i << " " << grid[j][i] << endl;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    sandCnt = 0;
    xmax = 665;
    ymax = 165;
    grid = vector<vector<char>>(ymax + 1, vector<char>(xmax + 1, '.'));

    int noOfPaths;
    cin >> noOfPaths;

    for (int i = 0; i < noOfPaths; i++) {
        int pathLen;
        cin >> pathLen;
        int oldX, oldY;
        cin >> oldX >> oldY;
        for (int j = 1; j < pathLen; j++) {
            int x, y;
            cin >> x >> y;

            draw(oldX, oldY, x, y);

            oldX = x;
            oldY = y;
        }
    }

     // draw the floor
    draw(0, 165, xmax, 165);

    // for (int row = 0; row < 10; row++) {
    //     for (int col = 494; col <= 503; col++) {
    //         cout << grid[row][col];
    //     }
    //     cout << endl;
    // }
    // cout << endl;

    simulate();

    // for (int row = 0; row < 10; row++) {
    //     for (int col = 494; col <= 503; col++) {
    //         cout << grid[row][col];
    //     }
    //     cout << endl;
    // }
    // cout << endl;

    cout << sandCnt << endl;
    return 0;
}
