#include <bits/stdc++.h>
using namespace std;

vector<double> gen() {
    srand(time(NULL));
    vector<double> l;
    l.reserve(1000000);
    for (int i = 0; i < 1000000; ++i) {
        double val = rand() + static_cast<double>(rand()) / RAND_MAX * 100000000000;    
        l.push_back(val);
    }
    
    return l;
}

int main() {
    for (int i = 1; i <= 10; ++i) {
        ofstream file("input" + to_string(i) + ".txt");
        vector<double> l = gen();
        if (i == 1) {
            sort(l.begin(), l.end());
        }
        if (i == 2) {
            sort(l.rbegin(), l.rend());
        }
        for (double j : l) {
            if ( static_cast<int64_t> (j)== j){
                file << static_cast<int64_t> (j) << " ";
            } else {
            file <<std::fixed << std::setprecision(8) << j << " ";
            }
        }
    }
    return 0;
}
