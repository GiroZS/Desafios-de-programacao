#include <stdio.h>

int main(){
    int n,result;
    int a,b;
    scanf("%d\n", &n);
    for(int i=0;i<n;i++){
        scanf("%d %d\n", &a,&b);
        result = a+b;
        printf("%d\n", result);
    }
        return 0;
}