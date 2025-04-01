#include <iostream>
#include <climits>
using namespace std;

int main() {
    const int ROWS = 5;
    const int COLS = 6;
    int arr[ROWS][COLS]{};

    cout << "Enter " << ROWS * COLS << " elements for the array:" << endl;
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            cout << "Element at position [" << i << "][" << j << "]: ";
            cin >> arr[i][j];
        }
    }

    int maxVal = INT_MIN;
    int minVal = INT_MAX;
    for (int i = 0; i < ROWS; ++i) {
        for (int j = 0; j < COLS; ++j) {
            if (arr[i][j] > maxVal) {
                maxVal = arr[i][j];
            }
            if (arr[i][j] < minVal) {
                minVal = arr[i][j];
            }
        }
    }

    cout << "Maximum value in the array: " << maxVal << endl;
    cout << "Minimum value in the array: " << minVal << endl;

    return 0;
}