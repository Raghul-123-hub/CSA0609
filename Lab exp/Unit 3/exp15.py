#include <stdio.h>

int main() {
    int a=1,b=7,c=3,d=5;
    int e=6,f=8,g=4,h=2;

    int M1=(a+d)*(e+h);
    int M2=(c+d)*e;
    int M3=a*(f-h);
    int M4=d*(g-e);
    int M5=(a+b)*h;
    int M6=(c-a)*(e+f);
    int M7=(b-d)*(g+h);

    int C11=M1+M4-M5+M7;
    int C12=M3+M5;
    int C21=M2+M4;
    int C22=M1-M2+M3+M6;

    printf("%d %d\n%d %d",C11,C12,C21,C22);

    return 0;
}
