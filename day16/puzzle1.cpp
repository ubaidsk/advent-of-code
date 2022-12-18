#include <iostream>
#include <set>
#include <map>
#include <vector>

using namespace std;

int curId;
map<string, int> ids;
map<int, string> stringIds;
vector<vector<int>> graph;
vector<int> flowRates;
map<vector<long long>, int> cache;

int getId(const string &s) {
    if (ids.find(s) == ids.end()) {
        ids[s] = curId++;
        stringIds[ids[s]] = s;
    }
    return ids[s];
}

int dfs(long long curNode, long long timeLeft, long long bit) {
    if (timeLeft <= 0) {
        return 0;
    }

    if (cache.find({curNode, timeLeft, bit}) != cache.end()) {
        return cache[{curNode, timeLeft, bit}];
    }

    int ans2 = 0;
    for (auto &neigh : graph[curNode]) {
        ans2 = max(ans2, dfs(neigh, timeLeft - 1, bit));
    }

    int ans1 = 0;
    if (flowRates[curNode] > 0 && (bit & (1LL << curNode)) == 0) {
        int flow = flowRates[curNode];
        flowRates[curNode] = 0;
        int newBit = bit | (1LL << curNode);
        for (auto &neigh : graph[curNode]) {
            ans1 = max(ans1, dfs(neigh, timeLeft - 2, newBit));
        }
        ans1 += (timeLeft - 1) * flow;
        flowRates[curNode] = flow;
    }

    int ans = max(ans1, ans2);
    cache[{curNode, timeLeft, bit}] = ans;
    return ans;
}

int main() {
    int n;
    cin >> n;
    flowRates = vector<int>(n);
    graph = vector<vector<int>>(n);
    for (int i = 0; i < n; i++) {
        string node;
        cin >> node;
        int flowRate;
        cin >> flowRate;
        flowRates[getId(node)] = flowRate;
        string neigh;
        cin >> neigh;
        while (neigh != "|") {
            graph[getId(node)].emplace_back(getId(neigh));
            cin >> neigh;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << stringIds[i] << "(" << flowRates[i] << "): ";
        for (auto &j:graph[i]) {
            cout << stringIds[j] << " ";
        }
        cout << endl;
    }

    int ans = dfs(getId("AA"), 30, 0);
    cout << ans << endl;
    return 0;
}
