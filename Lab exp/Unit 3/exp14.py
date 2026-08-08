#include <stdio.h>

int main() {
    int a[]={1,3,9,2,7,12};
    int n=6,target=15,found=0;

    for(int mask=0;mask<(1<<n);mask++) {
        int sum=0;

        for(int i=0;i<n;i++)
            if(mask&(1<<i))
                sum+=a[i];

        if(sum==target) {
            found=1;
            break;
        }
    }

    printf(found ? "true" : "false");

    return 0;
}
