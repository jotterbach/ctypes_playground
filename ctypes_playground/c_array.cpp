#include <iostream>
using namespace std;

extern "C" {
    int *get_array_ptr (int low, int length) {
        int *c = new int[length];
        for (int x = 0; x < length; x++) {
            c[x] = low + x;
        };
        return c;
    }

    int int_return (int x) {
        return x+1;
    }
}

int main() {
    int low = 1;
    int length = 4;

    int *arr_ptr = get_array_ptr(low, length);
    for (int x = 0; x < length; x++) {
        cout << arr_ptr[x] << endl;
    }
    return 0;
}
