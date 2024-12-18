# Solution
- The casino is using python's random module.
- We can exploit this using [randcrack](https://github.com/tna0y/Python-random-module-cracker), feeding it with 624 32-bit integers.
- The casino though generates 128-bit integers, but we need 32-bit integers to feed randcrack. The way 128-bit integers are generated is by concatenating 4 32-bit integers **right to left**.
- We split the 128-bit integers into 4 32-bit integers and feed them to randcrack.
```python
from pwn import *
from tqdm import tqdm
context.encoding='ascii'
t = remote('localhost',1337)
from randcrack import RandCrack
rc = RandCrack()

def submit():
    t.sendlineafter('choice: ','2')
    t.sendlineafter('ce): ','practice')
    t.sendlineafter('number > ','1')
    num=int(t.recvline().strip().split()[-1])
    num=bin(num)[2:].rjust(128,'0')
    nums=[int(num[i:i+32],2) for i in range(0,128,32)][::-1]
    for num in nums:
        rc.submit(num)  
    # print(nums)
    
def get_flag():
    t.sendlineafter('choice: ','2')
    t.sendlineafter('ce): ','play')
    t.sendlineafter('number > ',f'{rc.predict_getrandbits(128)}')
    t.sendlineafter('choice: ','3')
    print(t.recvline().strip().decode())
    
for _ in tqdm(range(624//4)):
    submit()
get_flag()
```