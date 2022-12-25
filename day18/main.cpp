#include <bits/stdc++.h>

using namespace std;

int noOfCubes;
map<vector<int>, int> cubeIdxMap;
map<vector<int>, vector<int>> graph;
vector<vector<vector<int>>> grid3D;

int xmax, ymax, zmax;
int outerSurfaceArea;

vector<vector<int>> getNeighs(int x, int y, int z) {
    vector<int> cell = {x, y, z};
    vector<int> cellMax = {xmax, ymax, zmax};

    vector<vector<int>> neighs;
    for (int i = 0; i < 3; i++) {
        vector<int> neigh = cell;
        neigh[i] += 1;
        if (neigh[i] >= 0 && neigh[i] < cellMax[i]) neighs.push_back(neigh);
        neigh[i] -= 2;
        if (neigh[i] >= 0 && neigh[i] < cellMax[i]) neighs.push_back(neigh);
    }
    return neighs;
}

void dfs(int x, int y, int z) {
    grid3D[x][y][z] = 2;
    for (auto &neigh:getNeighs(x, y, z)) {
        int X = neigh[0], Y = neigh[1], Z = neigh[2];
        if (grid3D[X][Y][Z] == -1) {
            dfs(X, Y, Z);
        } else if (grid3D[X][Y][Z] == 1) {
            outerSurfaceArea++;
        }
    }
}

int main() {
    cin >> noOfCubes;
    for (int i = 0; i < noOfCubes; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        x++;
        y++;
        z++;
        cubeIdxMap[{x, y, z}] = i + 1;
    }
    for (auto &cubeIdx:cubeIdxMap) {
        for (int i = 0; i < 3; i++) {
            vector<int> neigh = cubeIdx.first;
            neigh[i] += 1;
            if (cubeIdxMap.find(neigh) != cubeIdxMap.end()) {
                // neigh exists
                graph[cubeIdx.first].push_back(cubeIdxMap[neigh]);
            }
            neigh[i] -= 2;
            if (cubeIdxMap.find(neigh) != cubeIdxMap.end()) {
                // neigh exists
                graph[cubeIdx.first].push_back(cubeIdxMap[neigh]);
            }
        }
    }
    int surfaceArea = 0;
    for (auto &cubeIdx:cubeIdxMap) {
        surfaceArea += 6 - int(graph[cubeIdx.first].size());
    }

    cout << "puzzle1: " << surfaceArea << endl;


    outerSurfaceArea = 0;
    xmax = 24;
    ymax = 24;
    zmax = 24;

    grid3D = vector<vector<vector<int>>>(xmax, vector<vector<int>>(ymax, vector<int>(zmax, -1)));
    for (auto &cubeIdx: cubeIdxMap) {
        int x = cubeIdx.first[0], y = cubeIdx.first[1], z = cubeIdx.first[2];
        grid3D[x][y][z] = 1;
    }

    for (int x = 0; x < xmax; x++) {
        for (int y = 0; y < ymax; y++) {
            int z = 0;
            if (grid3D[x][y][z] == -1) {
                dfs(x, y, z);
            }
        }
        for (int y = 0; y < ymax; y++) {
            int z = zmax - 1;
            if (grid3D[x][y][z] == -1) {
                dfs(x, y, z);
            }
        }
    }


    for (int y = 0; y < ymax; y++) {
        for (int z = 0; z < zmax; z++) {
            int x = 0;
            if (grid3D[x][y][z] == -1) {
                dfs(x, y, z);
            }
        }
        for (int z = 0; z < zmax; z++) {
            int x = xmax - 1;
            if (grid3D[x][y][z] == -1) {
                dfs(x, y, z);
            }
        }
    }

    for (int z = 0; z < zmax; z++) {
        for (int x = 0; x < xmax; x++) {
            int y = 0;
            if (grid3D[x][y][z] == -1) {
                dfs(x, y, z);
            }
        }
        for (int x = 0; x < xmax; x++) {
            int y = ymax - 1;
            if (grid3D[x][y][z] == -1) {
                dfs(x, y, z);
            }
        }
    }

    cout << "puzzle2: " << outerSurfaceArea << endl;

    return 0;
}
