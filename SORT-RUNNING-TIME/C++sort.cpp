#include <bits/stdc++.h>
#include <chrono>
using namespace std;
using namespace chrono;
void sortVector(vector<double>& vec) {
     sort(vec.begin(), vec.end());
}

int main() {
    const int num_files = 10;
    const string file_prefix = "input"; // Tên tiền tố của các tập tin dữ liệu
    const string file_extension = ".txt"; // Phần mở rộng của tập tin dữ liệu
    const int num_values_per_file = 1000000; // Số lượng số thực trong mỗi tập tin

    // Sắp xếp từng tập tin dữ liệu
    for (int i = 1; i <= num_files; ++i) {
        string filename = file_prefix + to_string(i) + file_extension;
        ifstream file(filename);
        
        if (file.is_open()) {
            vector<double> values(num_values_per_file);
            for (int j = 0; j < num_values_per_file; ++j) {
                file >> values[j];
            }
            file.close();
        auto start_time = steady_clock::now();// Bắt đầu đo thời gian 
            sortVector(values);// Sắp xếp vector
            auto end_time = steady_clock::now();

            auto elapsed_time = duration_cast<microseconds>(end_time - start_time);
            cout << "Thoi gian chay cua tap tin " << filename << " la " << elapsed_time.count() << " microseconds" << endl;
        } else {
            std::cerr << "Error: Unable to open file " << filename << std::endl;
        }
    }

    return 0;
}
