#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string repeat_string(const string &str, int n) {
    string result = "";
    while (n-->0) {
        result += str;
    }
    return result;
}

int main() {
    int A, B;
    cin >> A >> B;
    if (B+1 > A || A > 2*B) {cout << "NO" << endl; return 0;}
    
    string mini = "aba";
    string gers = "ba";
    string answer = mini + repeat_string(gers, 2*B -A) + "\n";

    for (int i=0; i<A-B-1; i++) {
        answer += mini+"\n";
    }
    cout << "YES\n" << A-B << "\n" << answer;
    return 0;
}