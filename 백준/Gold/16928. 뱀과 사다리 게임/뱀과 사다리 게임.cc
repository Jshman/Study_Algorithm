#include <iostream>
#include <queue>
#include <map>

using namespace std;

map<int, int> ladder;
map<int, int> snake;

int board[101];

int main() {
    int n, m;
    cin >> n >> m;

    fill_n(board, 101, 100);

    // input ladder
    for (int i=0; i<n; i++) {
        int from, to;
        cin >> from >> to;
        ladder[from] = to;
    }

    // input snake
    for (int i=0; i<m; i++) {
        int from, to;
        cin >> from >> to;
        snake[from] = to;
    }

    int now = 1;
    board[now] = 0;
    queue<int> q;
    q.push(now);
    while (q.size()) {
        now = q.front();
        q.pop();
        
        // move
        for (int i=1; i<7; i++) {
            int next_pos = now + i;
            if (next_pos > 100) continue;
            
            // next_pos update
            if (ladder.count(next_pos)) {
                next_pos = ladder[next_pos];
            } else if (snake.count(next_pos)) {
                next_pos = snake[next_pos];
            } 
            
            // enqueue
            if (board[next_pos] == 100 || board[next_pos] > board[now] + 1) {
                board[next_pos] = board[now] + 1;
                q.push(next_pos);
            }   
        }        
    }

    cout << board[100] << endl;

    return 0;
}