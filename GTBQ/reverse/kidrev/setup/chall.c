#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdlib.h>

int main(){
    char input[100];
    printf("Enter the string to encrypt: ");
    scanf("%s", input);
    srand(1337);
    for (int i = 0; i < strlen(input); i++){
        int x=rand();
        x=x% 255;
        printf("%x ", (input[i]*x ^ (x)));
    }
}
