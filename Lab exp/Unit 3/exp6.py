#include <stdio.h>

void quickSort(int a[],int l,int h) {
    int i=l,j=h,pivot=a[(l+h)/2],temp;

    while(i<=j) {
        while(a[i]<pivot) i++;
        while(a[j]>pivot) j--;

        if(i<=j) {
            temp=a[i]; a[i]=a[j]; a[j]=temp;
            i++; j--;
        }
    }

    if(l<j) quickSort(a,l,j);
    if(i<h) quickSort(a,i,h);
}

int main() {
    int a[]={19,72,35,46,58,91,22,31};
    int n=8;

    quickSort(a,0,n-1);

    printf("Sorted array: ");
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);

    return 0;
}
