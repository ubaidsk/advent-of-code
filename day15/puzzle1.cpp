#include <iostream>
#include <set>

using namespace std;

int manhat_dist(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

int main() {
    int noOfSensors;
    cin >> noOfSensors;

    set<pair<int, int>> locsNoBeacon;
    set<pair<int, int>> locsSrcBeacon;

    for (int k = 0; k < noOfSensors; k++) {
        cout << "k: " << k << endl;
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        locsSrcBeacon.insert(make_pair(x1, y1));
        locsSrcBeacon.insert(make_pair(x2, y2));
        int dist = manhat_dist(x1, y1, x2, y2);

        if (abs(y1 - 2000000) <= dist) {
            int newDist = abs(y1 - 2000000);
            int distDiff = dist - newDist;
            // cout << "distDiff: " << distDiff << endl;
            for (int j = -distDiff; j <= distDiff; j++) {
                locsNoBeacon.insert(make_pair(x1 + j, 2000000));
            }
        }
    }

    for (auto &i:locsSrcBeacon) {
        locsNoBeacon.erase(i);
    }

    cout << locsNoBeacon.size() << endl;
    // for (auto &loc:locsNoBeacon) {
    //     cout << loc.first << " " << loc.second << endl;
    // }

    return 0;
}
