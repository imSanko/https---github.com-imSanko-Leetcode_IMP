#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

// Directions for BFS: (up, down, left, right)
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

bool is_valid(int x, int y, int N) {
    return x >= 0 && x < N && y >= 0 && y < N;
}

// BFS function to find the shortest path from 'S' to 'D'
int bfs(const vector<vector<char>>& grid, int N, pair<int, int> start, pair<int, int> end) {
    vector<vector<bool>> visited(N, vector<bool>(N, false));
    queue<pair<int, int>> q;
    visited[start.first][start.second] = true;
    q.push(start);
    int distance = 0;

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; ++i) {
            auto [x, y] = q.front();
            q.pop();

            if (x == end.first && y == end.second) {
                return distance;
            }

            for (int j = 0; j < 4; ++j) {
                int nx = x + dx[j];
                int ny = y + dy[j];
                if (is_valid(nx, ny, N) && !visited[nx][ny] && grid[nx][ny] == 'T') {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
        ++distance;
    }

    return -1; // If there's no valid path
}

// Main function to solve the problem
int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<char>> grid(N, vector<char>(N));
    vector<pair<int, int>> sheets;

    int sx, sy, dx, dy; // coordinates of 'S' and 'D'
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
            if (grid[i][j] == 'S') {
                sx = i;
                sy = j;
            }
            if (grid[i][j] == 'D') {
                dx = i;
                dy = j;
            }
        }
    }

    // Perform BFS to find the shortest path from 'S' to 'D'
    int result = bfs(grid, N, {sx, sy}, {dx, dy});
    
    cout << result << endl;
    
    return 0;
}
