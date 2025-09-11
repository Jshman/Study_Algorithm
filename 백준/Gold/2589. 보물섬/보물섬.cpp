#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

// global vector
vector<string> grid;
// dxys - NESW
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

int bfs(int L, int W, int i, int j) {
    // make visited vector
    vector<vector<int>> visited(L, vector<int>(W, 0));
    visited[i][j] = 1;

    queue<pair<int, int>> q;
    q.push(make_pair(i, j));

    int dist = -1;
    while (q.size()) {
        auto [y, x] = q.front();
        q.pop();
        dist = max(dist, visited[y][x]);

        for (int d=0; d<4; d++){
            int ny = dy[d] + y;
            int nx = dx[d] + x;
            if ((0<=ny && ny<L && 0<=nx && nx<W) && grid[ny][nx]=='L' && visited[ny][nx] == 0) {
                visited[ny][nx] = visited[y][x] + 1;
                q.push(make_pair(ny, nx));
            }
        }
    }

    return dist - 1;
}


int main() {
    // input
    int L, W;
    cin >> L >> W;

    // grid initial and visited
    for (int i=0; i<L; i++) {
        string input;
        cin >> input;
        grid.push_back(input);
    }

    //bfs
    int answer = 0;
    for (int i=0; i<L; i++) {
        for (int j=0; j<W; j++){
            if (grid[i][j] == 'L') {
                int dist = bfs(L, W, i, j);
                answer = max(answer, dist);
            }
        }
    }
    cout << answer << endl;

    return 0;
}
