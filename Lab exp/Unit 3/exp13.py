#include <stdio.h>
#include <stdlib.h>

int main() {
    int a[]={45,34,4,12,5,2};
    int n=6,target=42;
    int best=0,diff=999999,mask;

    for(mask=0;mask<(1<<n);mask++) {
        int sum=0;
        for(int i=0;i<n;i++)
            if(mask&(1<<i)) sum+=a[i];

        if(abs(target-sum)<diff) {
            diff=abs(target-sum);
            best=sum;
        }
    }

    printf("Closest Sum = %d\nDifference = %d",best,diff);
    return 0;
}
