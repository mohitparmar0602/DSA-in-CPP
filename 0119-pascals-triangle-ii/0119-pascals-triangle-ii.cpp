#include <vector>

class Solution {
public:
    std::vector<int> getRow(int rowIndex) {
        std::vector<int> row(rowIndex + 1, 1);
        for (int i = 1; i <= rowIndex; ++i) {
            row[i] = static_cast<int>(static_cast<long long>(row[i - 1]) * (rowIndex - i + 1) / i);
        }
        return row;
    }
};