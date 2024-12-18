# Solution:
- Bob sends the same message to Alice, Eve and Emily.
- Using this [website](https://8gwifi.org/PemParserFunctions.jsp) that Alice, Eve and Emily have the same small exponent `e=3`. 
- Since we have `3=e` different ciphertexts, we can perform the [Hastad's Broadcast Attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#H.C3.A5stad.27s_broadcast_attack) to recover the plaintext.
```python
from Crypto.PublicKey import RSA
from libnum import solve_crt #solve_crt(rems,moduli)
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot
# The 3 public keys
A='''-----BEGIN PUBLIC KEY-----...'''
B='''-----BEGIN PUBLIC KEY-----...'''
C='''-----BEGIN PUBLIC KEY-----...''''
# the 3 ciphertexts
a,b,c=...
# crt
n1=RSA.importKey(A).n
n2=RSA.importKey(B).n
n3=RSA.importKey(C).n
e=3
m_e=solve_crt([a,b,c],[n1,n2,n3])
m=iroot(m_e,e)[0]
print(long_to_bytes(m).decode())
```