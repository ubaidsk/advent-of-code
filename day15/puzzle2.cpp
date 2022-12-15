#include <iostream>
#include <vector>
#include <map>

using namespace std;

int minBoundaryLimit, maxBoundaryLimit;

int manhat_dist(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

int main() {
    minBoundaryLimit = 0;
    // maxBoundaryLimit = 20;
    maxBoundaryLimit = 4000000;

    int noOfSensors;
    cin >> noOfSensors;

    vector<pair<int, int>> sensorLocs, beaconLocs;

    for (int k = 0; k < noOfSensors; k++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        sensorLocs.push_back({x1, y1});
        beaconLocs.push_back({x2, y2});
    }

    for (int row = 0; row < maxBoundaryLimit; row++) {
        map<int, int> colRange;

        // for (auto &s : sensorLocs) {
        //     if (s.second == row) {
        //         colRange[s.first]++;
        //         colRange[s.first + 1]--;
        //     }
        // }

        // for (auto &s : beaconLocs) {
        //     if (s.second == row) {
        //         colRange[s.first]++;
        //         colRange[s.first + 1]--;
        //     }
        // }

        for (int i = 0; i < noOfSensors; i++) {
            auto &sensor = sensorLocs[i];
            auto &beacon = beaconLocs[i];
            int dist = manhat_dist(sensor.first, sensor.second, beacon.first,
                                   beacon.second);
            int rowDist = abs(sensor.second - row);
            int distDiff = dist - rowDist;
            // cout << "distDiff: " << distDiff << endl;
            int l = max(sensor.first - distDiff, minBoundaryLimit),
                r = min(sensor.first + distDiff, maxBoundaryLimit);
            if (l <= r) {
                colRange[l]++;
                colRange[r + 1]--;
            }
        }

        int cur = 0;
        for (auto &i : colRange) {
            cur += i.second;
            if (i.first != (maxBoundaryLimit + 1) && cur == 0) {
                cout << i.first << " " << row << endl;
            }
        }
    }

    return 0;
}
