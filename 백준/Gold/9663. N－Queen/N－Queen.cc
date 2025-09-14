#include <iostream>
#include <vector>

using namespace std;

int N;
vector<vector<int>> board;

bool widthAndLength(int y, int x) {
    for (int j=0; j<N; j++) 
        if (board[y][j] == 1) return false;
    
    for (int i=0; i<N; i++)
        if (board[i][x] == 1) return false;
    return true;
}

bool diagonal(int y, int x) {
    // 우상향
    for (int i=y, j=x; (0<=i && j<N); i--, j++){
        if (i==y && j==x) continue;
        if (board[i][j] == 1) return false;}
    // 우하향
    for (int i=y, j=x; (i<N && j<N); i++, j++){
        if (i==y && j==x) continue;
        if (board[i][j] == 1) return false;}
    // 좌상향
    for (int i=y, j=x; (0<=i && 0<=j); i--, j--){
        if (i==y && j==x) continue;
        if (board[i][j] == 1) return false;}
    // 좌하향
    for (int i=y, j=x; (i<N && 0<=j); i++, j--){
        if (i==y && j==x) continue;
        if (board[i][j] == 1) return false;}
    return true;
}

bool isFine(int i, int j) {
    return widthAndLength(i, j) && diagonal(i, j);
}

int btk(int y=0, int cnt_Queen=0, int depth=0) {
    if (depth == N && cnt_Queen == N) return 1;
    if (y >= N || cnt_Queen != depth) return 0;

    int ret = 0;
    for (int i=0; i<N; i++) {
        if (isFine(y, i)) {
            board[y][i] = 1;
            ret += btk(y+1, cnt_Queen+1, depth+1);
        }
        board[y][i] = 0;
    }
    return ret;
}

int main() {
    cin >> N;
    
    /* 
    0: 빈 칸
    1: 퀸
    */
    board = vector<vector<int>>(N, vector<int>(N, 0));
    cout << btk() << endl;
    return 0;
} 