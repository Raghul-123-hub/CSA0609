#include <stdio.h>

int main() {
    int a[]={5,10,15,20,25,30,35,40,45};
    int n=9,key=20;
    int low=0,high=n-1,mid,pos=-1,count=0;

    while(low<=high) {
        mid=(low+high)/2;
        count++;

        if(a[mid]==key) {
            pos=mid+1;
            break;
        }
        else if(a[mid]<key)
            low=mid+1;
        else
            high=mid-1;
    }

    printf("Position = %d\nComparisons = %d",pos,count);

    return 0;
}
