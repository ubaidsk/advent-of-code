#include <bits/stdc++.h>
using namespace std;

struct Node {
    string name;
    long long val;
    char opt;
    bool end = false;
    string left, right;
    Node(string n, char o, bool e, string l, string r): name(n), opt(o), end(e), left(l), right(r) {}
    Node(string n, long long v, bool e): name(n), val(v), end(e) {}
};

map<string, Node*> nodes;


long long dfs(string cur) {
    Node* n = nodes[cur];
    if (n->end) return n->val;
    long long lval = dfs(n->left), rval = dfs(n->right);
    switch (n->opt) {
        case '+': n->val = lval + rval; break;
        case '-': n->val = lval - rval; break;
        case '*': n->val = lval * rval; break;
        case '/': n->val = lval / rval; break;
    }
    n->end = true;
    return n->val;
}

bool getPath(string cur, string des, vector<int> &path) {
    cout << "------ getPath (" << cur << ") ----" << endl;
    Node* n = nodes[cur];
    if (n->name == des) {
        return true;
    }

    if (n->end) {
        return false;
    }

    path.emplace_back(0);
    if (getPath(n->left, des, path)) {
        return true;
    }
    path.pop_back();

    path.emplace_back(1);
    if (getPath(n->right, des, path)) {
        return true;
    }
    path.pop_back();

    return false;
}

void computeHumnVal(string cur, long long val, int idx, vector<int> &path) {
    Node *n = nodes[cur];
    while (idx < path.size()) {
        if (path[idx]) {
            long long lval = dfs(n->left);
            long long rval;
            switch(n->opt) {
                case '+': rval = val - lval; break;
                case '-': rval = lval - val; break;
                case '*': rval = val / lval; break;
                case '/': rval =  lval / val; break;
                case '=': rval = lval; break;
            }
            n = nodes[n->right];
            val = rval;
        } else {
            long long rval = dfs(n->right);
            long long lval;
            switch (n->opt) {
                case '+': lval = val - rval; break;
                case '-': lval = val + rval; break;
                case '*': lval = val / rval; break;
                case '/': lval = val * rval; break;
                case '=': lval = rval; break;
            }
            n = nodes[n->left];
            val = lval;
        }
        idx++;
    }

    cout << n->name << ": " << n->val << " " << val << endl;
}

int main() {
    string input;
    while(getline(cin, input)) {
        if (input.size() == 17) {
            string node = input.substr(0, 4);
            string left = input.substr(6, 4);
            char opt = input[11];
            string right = input.substr(13, 4);
            nodes[node] = new Node(node, opt, false, left, right);

        } else {
            string node = input.substr(0, 4);
            long long val = stoi(input.substr(6));
            nodes[node] = new Node(node, val, true);
        }
    }

    vector<int> path;
    if (getPath("root", "humn", path)) {
        cout << "Found" << endl;
    }

    nodes["root"]->opt = '=';
    computeHumnVal("root", 0LL, 0, path);
    cout << nodes["humn"]->val << endl;

    return 0;
}
