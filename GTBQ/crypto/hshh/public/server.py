from hashlib import sha256
from itertools import cycle
from secret import FLAG
def xor(a:bytes, b:bytes)->bytes:
    if len(a)<len(b): # make sure a >= b
        a,b=b,a
    return bytes([x^y for x,y in zip(a,cycle(b))])


def H(s:bytes)->bytes:
    return sha256(s).digest()

def encrypt(msg:str,key='🤫🤫🤫')->str:
    key = key.encode()
    key = H(key)
    msg = msg.encode()
    for _ in range(1000):
        key = H(key)
        msg = xor(msg, key)
    return msg.hex()

    
if __name__ == '__main__':
    print('Select an option:')
    while True:
        choice=input('1. Encrypt\n2. Get encrypted flag\n3. Exit\n')
        if choice == '1':
            msg=input('Enter the message to encrypt: ')
            print(encrypt(msg))
        elif choice == '2':
            print(encrypt(FLAG))
        elif choice == '3':
            exit()
        else:
            print('Invalid choice')