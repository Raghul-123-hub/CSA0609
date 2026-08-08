#include <stdio.h>

void sort(int a[],int n) {
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
            if(a[i]>a[j]) {
                int t=a[i]; a[i]=a[j]; a[j]=t;
            }
}

int median_of_medians(int a[],int n,int k) {
    sort(a,n);
    return a[k-1];
}

int main() {
    int a[]={23,17,31,44,55,21,20,18,19,27};
    int n=10,k=5;

    printf("K-th smallest element = %d",
           median_of_medians(a,n,k));

    return 0;
}
