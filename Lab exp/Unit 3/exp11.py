#include <stdio.h>

void sort(int a[],int n) {
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
            if(a[i]>a[j]) {
                int t=a[i]; a[i]=a[j]; a[j]=t;
            }
}

int selectK(int a[],int n,int k) {
    sort(a,n);
    return a[k-1];
}

int main() {
    int a[]={12,3,5,7,19};
    int n=5,k=2;

    printf("K-th smallest = %d",selectK(a,n,k));

    return 0;
}
