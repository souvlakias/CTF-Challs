#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdlib.h>


/* python
print(f'int out[{len(out)}] = {"{"}',end=' ')
for o in out:
    print(f'{int(o,16)}, ',end=' ')
print('};')
*/

int main(){
    int out[22] = { 7270,  8478,  4357,  18144,  2960,  24699,  6242,  29908,  400,  10769,  12512,  11488,  9831,  12381,  13176,  8320,  8332,  286,  11349,  9556,  12074,  12960,  };
    srand(1337);
    for (int i = 0; i < 22; i++){
        int x=rand();
        x=x% 255;
        printf("%c", (out[i] ^ (x))/x);
    }
}
