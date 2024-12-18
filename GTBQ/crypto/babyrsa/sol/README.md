# Solution:
- We can find all the factors one by one by getting the GCD of the moduli.


```python
from Crypto.Util.number import bytes_to_long, long_to_bytes, GCD
n = ...
v = ...
w = ...
c2 = ...
c3 = ...
e = 65537

def decrypt(c:int, n, prime_factors:list): # decrypt message if we know the prime factors of n
    phi=1
    for p in prime_factors:
        phi*=(p-1)
    d=pow(e, -1, phi)
    m=pow(c, d, n)
    return long_to_bytes(m).decode()


q= GCD(n, v) 
p= n//q
r= v//q
k= w//(p*q*r)

print(decrypt(c2, v, [q,r]), end='')
print(decrypt(c3, w, [p,q,r,k]))
```