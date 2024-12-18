from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from secret import FLAG

def encrypt(m:str, e, n): # encrypt message with public key
    m=m.encode() # convert to bytes
    m=bytes_to_long(m) # convert to integer
    return pow(m, e, n)

def decrypt(c:int, n, prime_factors:list): # decrypt message if we know the prime factors of n
    phi=1
    for p in prime_factors:
        phi*=(p-1)
    d=pow(e, -1, phi)
    m=pow(c, d, n)
    return long_to_bytes(m).decode()


if __name__ == '__main__':
    e=65537
    p=getPrime(512)
    q=getPrime(512)
    n=p*q


    r=getPrime(512)
    v=q*r

    k=getPrime(512)
    w=p*q*r*k

    print(f'{n = }')
    print(f'{v = }')
    print(f'{w = }')

    # print(f'c1 = {encrypt(FLAG, e, n)}')
    print(f'c2 = {encrypt(FLAG[:20], e, v)}')
    print(f'c3 = {encrypt(FLAG[20:], e, w)}')