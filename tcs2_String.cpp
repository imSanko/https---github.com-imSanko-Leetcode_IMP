#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
https://telegram.me/+_hn3cBQVbGliYTI9

using namespace std;

int dp(string& s, vector<string>& v, unordered_map<string, int>& memo) {
    
    if (memo.count(s)) return memo[s];
// @PLACEMENTLELO
    int placementlelo = 0;
https://telegram.me/+_hn3cBQVbGliYTI9

    for (auto& x : v) {
        size_t pos = s.find(x); 
// @PLACEMENTLELO
        if (pos != string::npos) {
            string new_string = s.substr(0, pos) + s.substr(pos + x.size());
            placementlelo = max(placementlelo, 1 + dp(new_string, v, memo));
        }
    }
// @PLACEMENTLELO
    return memo[s] = placementlelo;
}

int main() {
    int n;
    cin >> n;
// @PLACEMENTLELO
    vector<string> substrings(n);
    for (int i = 0; i < n; ++i) {
        cin >> substrings[i];
    }
https://telegram.me/+_hn3cBQVbGliYTI9

    string mainString;
    cin >> mainString;
// @PLACEMENTLELO
    unordered_map<string, int> memo;

    cout << dp(mainString, substrings, memo) << endl;

    return 0;
}