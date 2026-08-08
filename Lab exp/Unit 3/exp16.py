#include <stdio.h>

long long karatsuba(long long x,long long y) {
    if(x<10 || y<10)
        return x*y;

    long long p=1;
    long long temp=x;

    while(temp>=10) {
        p*=10;
        temp/=10;
    }

    long long a=x/p;
    long long b=x%p;
    long long c=y/p;
    long long d=y%p;

    long long z2=karatsuba(a,c);
    long long z0=karatsuba(b,d);
    long long z1=karatsuba(a+b,c+d)-z2-z0;

    return z2*p*p+z1*p+z0;
}

int main() {
    long long x=1234,y=5678;

    printf("Product = %lld",karatsuba(x,y));

    return 0;
}
