#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int N, M, T;
vector<vector<int>> grid;

int princess[2] = {-1, -1};
int gram[2] = {-1, -1};
int gram_to_princess = -1;

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

void cal_gram() {
    gram_to_princess = abs(princess[0]-gram[0]) + abs(princess[1]-gram[1]);
}

int bfs(int i=0, int j=0, int time=0) {
    vector<bool> visited = vector<bool>(N*M, false);
    queue<vector<int>> q;
    q.push({i, j, time});
    
    bool get_gram = false;
    int when_get_gram = 10001;
    int meet_princess = 10001;

    while (q.size()) {
        int y, x, t;
        y = q.front()[0];
        x = q.front()[1];
        t = q.front()[2];
        q.pop();
        if (visited[y*M+x]) continue;
        visited[y*M + x] = true;
        if (T < t) continue;
        
        if (y == gram[0] && x == gram[1]) {
            get_gram = true;
            when_get_gram = min(when_get_gram, t);
        }
        if (y == princess[0] && x == princess[1]){
            meet_princess = min(t, meet_princess);
        }

        for (int d=0; d<4; d++) {
            int ny = y+dy[d];
            int nx = x+dx[d];
            if (!(0<=ny && ny<N && 0<=nx && nx<M) || visited[ny*M + nx] || grid[ny][nx] == 1) continue;
            q.push({ny, nx, t+1});
            grid[ny][nx] = t+1;
        }
    }
    if (get_gram) return min(when_get_gram + gram_to_princess, meet_princess);
    return meet_princess;
}

int main() {
    cin >> N >> M >> T;
    grid = vector<vector<int>>(N, vector<int>(M, 0));

    // 격자 입력
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            int input;
            cin >> input;
            grid[i][j] = input;
            if (input == 2) {
                gram[0] = i;
                gram[1] = j;
            }
        }
    }
    
    princess[0] = N-1; princess[1] = M-1;
    cal_gram();

    int times = bfs();
    if (times > 10000 || times > T)
        cout << "Fail" << endl;
    else
        cout << times << endl;
    return 0;
}