#include <stdio.h>

int main() {
    int a[] = {5,7,3,4,9,12,6,2};
    int n = 8, min = a[0], max = a[0];

    for(int i=1;i<n;i++) {
        if(a[i] < min) min = a[i];
        if(a[i] > max) max = a[i];
    }

    printf("Min = %d\nMax = %d", min, max);
    return 0;
}
