#include <stdio.h>

int parent(int idx) {
    return (idx - 1) / 2;
}

int lchild(int idx) {
    return (idx * 2 + 1);
}

int rchild(int idx) {
    return (idx * 2 + 2);
}

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

class heap {
    int arr[200]; // Can handle up to 200 elements
    int length;

public:
    heap() : length(0) {}

    void push(int value) {
        arr[length] = value;
        int idx = length++;
        while (idx > 0 && arr[idx] > arr[parent(idx)]) {
            swap(&arr[idx], &arr[parent(idx)]);
            idx = parent(idx);
        }
    }

    void pop() {
        if (length == 0) return; // Avoid underflow

        arr[0] = arr[--length];
        int idx = 0;

        while (lchild(idx) < length) { // Ensure left child exists
            int largest = idx;
            if (arr[lchild(idx)] > arr[largest]) {
                largest = lchild(idx);
            }
            if (rchild(idx) < length && arr[rchild(idx)] > arr[largest]) {
                largest = rchild(idx);
            }
            if (largest == idx) break; // Stop if already in place

            swap(&arr[idx], &arr[largest]);
            idx = largest;
        }
    }

    int size() {
        return length;
    }

    void display() { // Displays in array format
        for (int i = 0; i < length; i++)
            printf("%d ", arr[i]);
        printf("\n");
    }
};

int main() {
    heap x;
    x.push(9);
    x.push(100);
    x.push(20);
    x.pop();
    x.display(); // Expected Output: 20 9
}
