#include <stdio.h>

int main() {
    int a[]={3,9,14,19,25,31,42,47,53};
    int n=9,key=31;
    int low=0,high=n-1,mid;

    while(low<=high) {
        mid=(low+high)/2;
        printf("Low=%d High=%d Mid=%d Value=%d\n",
               low+1,high+1,mid+1,a[mid]);

        if(a[mid]==key) {
            printf("Element found at position %d",mid+1);
            return 0;
        }

        if(a[mid]<key)
            low=mid+1;
        else
            high=mid-1;
    }

    printf("Element not found");
    return 0;
}
