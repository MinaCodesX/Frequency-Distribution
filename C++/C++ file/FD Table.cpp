#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

struct FrequencyTableRow {
    string Class;
    int Frequency;
    double Relative_Frequency;
    double Midpoint;
    int Cumulative_Frequency;
};

vector<FrequencyTableRow> create_frequency_table(vector<int> data, int K = 6) {

    sort(data.begin(), data.end());

    vector<int> class_start;
    for (int i = 0; i < K; ++i) {
        class_start.push_back(data[0] + 10 * i);
    }

    vector<FrequencyTableRow> frequency_table;

    int cumulative_sum = 0;
    for (int i = 0; i < K; ++i) {

        int frequency = count_if(data.begin(), data.end(), [&](int x) { return x >= class_start[i] && x < class_start[i] + 10; });

        double midpoint = (class_start[i] + class_start[i] + 10) / 2.0;

        double relative_frequency = static_cast<double>(frequency) / data.size();

        cumulative_sum += frequency;

        frequency_table.push_back({ to_string(class_start[i]) + " - " + to_string(class_start[i] + 10),
                                    frequency,
                                    relative_frequency,
                                    midpoint,
                                    cumulative_sum });
    }

    int R = data.back() - data.front();
    cout << "R: " << R << endl;
    cout << "K: " << K << endl;
    cout << "Rules for Class Width (W):" << endl;
    cout << "1. W = (Max - Min) / K" << endl;
    cout << "2. Choose a value for K based on the desired number of classes." << endl;
    cout << "3. Calculate class width (W) using the formula." << endl;
    cout << "4. Round up the class width to the nearest convenient number." << endl;
    cout << "5. Ensure all data points fall within the classes." << endl;

    return frequency_table;
}

int main() {
    vector<int> data = { 62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
                         84, 73, 93, 64, 89 };
    int K = 6;
    vector<FrequencyTableRow> frequency_table = create_frequency_table(data, K);

    cout << setw(30) << "Class" << setw(15) << "Frequency" << setw(25) << "Relative Frequency" << setw(15) << "Midpoint" << setw(25) << "Cumulative Frequency" << endl;
    for (const auto& row : frequency_table) {
        cout << setw(30) << row.Class << setw(15) << row.Frequency << setw(25) << row.Relative_Frequency << setw(15) << row.Midpoint << setw(25) << row.Cumulative_Frequency << endl;
    }

    return 0;
}