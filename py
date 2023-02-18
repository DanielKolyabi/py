30
#include <iostream>
using namespace std;
 
int main() {
    int mas[10];
    int iDelta = 0x0;
    cin >> mas[0] >> iDelta;
    for(int i = 1; i < 10; i++){
        mas[i] = mas[i - 1] + iDelta;
        cout << mas[i - 1] << " ";
    }
    cout << mas[10];
    return 0;
}
32
from random import randint
 
lo, hi = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Original array:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("Indexes:", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Remaining elements:", data, sep='\n')
print("Required elements:", result, sep='\n')
