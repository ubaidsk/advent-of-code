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

    long long val = dfs("root");
    cout << val << endl;

    return 0;
}
