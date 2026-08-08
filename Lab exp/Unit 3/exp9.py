#include <stdio.h>

void sort(int p[][2],int n) {
    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++) {
            int d1=p[i][0]*p[i][0]+p[i][1]*p[i][1];
            int d2=p[j][0]*p[j][0]+p[j][1]*p[j][1];

            if(d1>d2) {
                int x=p[i][0],y=p[i][1];
                p[i][0]=p[j][0]; p[i][1]=p[j][1];
                p[j][0]=x; p[j][1]=y;
            }
        }
}

int main() {
    int p[4][2]={{1,3},{-2,2},{5,8},{0,1}};
    int n=4,k=2;

    sort(p,n);

    printf("Closest points: ");
    for(int i=0;i<k;i++)
        printf("[%d,%d] ",p[i][0],p[i][1]);

    return 0;
}
