#include <iostream>
#include <string>

using namespace std;

int main() {
    int sum = 0;
    int arr[100] = {0,}; // init array to 0
    int mode = 0;

    for (int i=0; i<10; i++) {
        int num;
        cin >> num;
        sum += num;
        arr[num/10]++;
        if (arr[num/10] > arr[mode/10]) {
            mode = num;
        }
    }

    cout << sum/10 << "\n" << mode << endl;
    return 0;
}