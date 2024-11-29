#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Function to recursively remove substrings and count the maximum removals
int max_removals(string main_string, const vector<string>& substrings, vector<bool>& used_substrings) {
    int max_removed = 0;

    // Try removing each substring and recursively calculate the maximum removals
    for (size_t i = 0; i < substrings.size(); ++i) {
        // Skip if the substring has already been used
        if (used_substrings[i]) {
            continue;
        }

        // Find the substring in the main string
        size_t pos = main_string.find(substrings[i]);
        if (pos != string::npos) {
            // Mark the substring as used
            used_substrings[i] = true;

            // Remove the substring from the main string
            string new_string = main_string.substr(0, pos) + main_string.substr(pos + substrings[i].length());

            // Recursively calculate the number of removals with the updated string
            max_removed = max(max_removed, 1 + max_removals(new_string, substrings, used_substrings));

            // Mark the substring as unused for other recursive calls
            used_substrings[i] = false;
        }
    }

    return max_removed;
}

int main() {
    size_t N;
    cin >> N;  // Number of substrings
    cin.ignore();  // To ignore the newline character after reading N

    vector<string> substrings(N);
    for (size_t i = 0; i < N; ++i) {
        cin >> substrings[i];  // Reading each substring
    }

    string main_string;
    cin >> main_string;  // The main string to be modified

    // Vector to keep track of used substrings
    vector<bool> used_substrings(N, false);

    // Calling the function to calculate the maximum number of substrings that can be removed
    int result = max_removals(main_string, substrings, used_substrings);

    // Output the result
    cout << result << endl;

    return 0;
}


///corrent code 
