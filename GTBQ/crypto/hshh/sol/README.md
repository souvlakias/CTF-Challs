# Solution:

```python
for _ in range(1000):
    key = H(key)
    msg = xor(msg, key)
return msg.hex()
```
- We have something like:
    - enc = msg $ \oplus (H(key) \oplus H(H(key)) \oplus ... \oplus H^{1000}(key)) $
- Since the app is using the same key each time we have a constant 
    $ (H(key) \oplus H(H(key)) \oplus ... \oplus H^{1000}(key)) = h $
- Requesting ```encrypt('\0'*100)``` we get `enc = msg ^ h = h`, since `msg=0`
- Since we know `h`, we request the enc_flag and xor it with `h`.

```python
from pwn import *
context.encoding='ascii'
t = remote('localhost',1337)
def send_hex_msg(data):
    t.sendlineafter('ce: ','1')
    t.sendlineafter('rypt: ',data)
    return bytes.fromhex(t.recvline().strip().decode())

def get_enc_flag():
    t.sendlineafter('ce: ','2')
    return bytes.fromhex(t.recvline().strip().decode())

X=send_hex_msg('\0'*100) 
enc=get_enc_flag()
flag=xor(X,enc)
print(flag)
```