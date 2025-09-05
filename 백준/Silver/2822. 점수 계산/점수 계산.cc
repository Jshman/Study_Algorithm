#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    vector<pair<int, int>> scores;
    for (int i=0; i<8; ++i) {
        int score;
        cin >> score;
        scores.push_back(pair<int, int>(score, i+1));
    }
    sort(scores.begin(), scores.end());
    
    vector<int> selected;
    int sum = 0;
    for (int i=0; i<5; i++) {
        sum += scores[i+3].first;
        selected.push_back(scores[i+3].second);
    }

    sort(selected.begin(), selected.end());
    cout << sum << "\n";
    for (int i=0; i<5; i++) {
        cout << selected[i] << " ";
    }

    return 0;
}