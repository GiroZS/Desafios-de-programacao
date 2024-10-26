#include <stdio.h>

int main(){
    int n;
    int k;
    int result = 1;
    scanf("%d\n%d",&n,&k);
    for(int i=0;i<n;i++){
        if(result>k){
            result=result+k;
        }else{
            result = 2*result;
        }
    }
    printf("%d", result);
    return 0;
}