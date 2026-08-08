#include <stdio.h>

int main() {
    int A[]={1,2},B[]={-2,-1},C[]={-1,2},D[]={0,2};
    int n=2,count=0;

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            for(int k=0;k<n;k++)
                for(int l=0;l<n;l++)
                    if(A[i]+B[j]+C[k]+D[l]==0)
                        count++;

    printf("Number of tuples = %d",count);
    return 0;
}
