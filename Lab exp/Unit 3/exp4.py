#include <stdio.h>

int count=0;

void merge(int a[],int l,int m,int r) {
    int b[100],i=l,j=m+1,k=0;

    while(i<=m && j<=r) {
        count++;
        if(a[i]<=a[j]) b[k++]=a[i++];
        else b[k++]=a[j++];
    }

    while(i<=m) b[k++]=a[i++];
    while(j<=r) b[k++]=a[j++];

    for(i=l,k=0;i<=r;i++,k++)
        a[i]=b[k];
}

void mergeSort(int a[],int l,int r) {
    if(l<r) {
        int m=(l+r)/2;
        mergeSort(a,l,m);
        mergeSort(a,m+1,r);
        merge(a,l,m,r);
    }
}

int main() {
    int a[]={12,4,78,23,45,67,89,1};
    int n=8;

    mergeSort(a,0,n-1);

    printf("Sorted array: ");
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);

    printf("\nComparisons = %d",count);
    return 0;
}
