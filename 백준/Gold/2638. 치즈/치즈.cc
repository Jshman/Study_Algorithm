#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// grid size
int N, M;
vector<vector<int>> grid;

// dxys - NESW
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

bool isMeltedCheese(int i, int j) {
    int cnt = 0;
    for (int d=0; d<4; d++) {
        int ny = i + dy[d];
        int nx = j + dx[d];
        if (!(0<=ny && ny<N && 0<=nx && nx<M)) continue;
        if (grid[ny][nx] == 3) cnt++;
    }
    return cnt >= 2;
}

void outter(int i, int j, vector<vector<bool>> &visited){
    queue<pair<int, int>> q;
    q.push(make_pair(i, j));
    while (q.size()) {
        auto [y, x] = q.front();
        q.pop();
        if(visited[y][x]) continue;
        visited[y][x] = true;
        grid[y][x] = 3;

        for (int d=0; d<4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (!(0<=ny && ny<N && 0<=nx && nx<M) || visited[ny][nx]) continue;
            if (grid[ny][nx] == 0 || grid[ny][nx] == 3) q.push(make_pair(ny, nx));
        }
    }
}


/* state 
    0 : inner air
    1 : cheese
    2 : melting cheese
    3 : outter air
*/
int main() {
    // input gird size
    cin >> N >> M;
    grid = vector<vector<int>>(N,vector<int>(M, 0));
    vector<vector<bool>> visited;
    
    // input gird
    for (int i=0; i<N; i++)
        for (int j=0; j<M; j++)
            cin >> grid[i][j];
    
    int ans = -1;
    bool condition = true;
    while (condition) {
        ans++;
        condition = false;

        visited.assign(N, vector<bool>(M, false));

        outter(0, 0, visited);
        outter(0, N-1, visited);
        outter(N-1, 0, visited);
        outter(N-1, N-1, visited);

        // 녹을 치즈에 표시
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (grid[i][j] == 1 && isMeltedCheese(i, j)) {
                    grid[i][j] = 2;
                    condition = true;
                }
            }
        }
        // 치즈 녹이기
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (grid[i][j] == 2) grid[i][j] = 3; 
            }
        }
    }

    cout << ans << endl;

    return 0;
}