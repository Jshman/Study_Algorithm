#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

int main() {
    int K;
    cin >> K;

    for (int i=0; i<K; i++) {
        int N;
        cin >> N;
        
        vector<int> scores;
        for (int j=0; j<N; j++) {
            int score;
            cin >> score;
            scores.push_back(score);
        }
        sort(scores.begin(), scores.end(), greater<int>());

        int largest_gap = -1;
        for (int i=1; i<N; i++) {
            largest_gap = max(largest_gap, abs(scores[i] - scores[i-1]));
        }

        // string ans = std::format("Class {0}\nMax {1}, Min {2}, Largest gap {3}", i+1, scores[0], scores[N-1], largest_gap);
        std::stringstream ans;
        ans << "Class " << i+1 << "\nMax " << scores[0] << ", Min " << scores[N-1] << ", Largest gap " << largest_gap;
        
        std::string ss = ans.str();

        std:: cout << ss << std::endl;
    }

    return 0;
}