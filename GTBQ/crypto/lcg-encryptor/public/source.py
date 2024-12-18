import random
p=594682003472506879
print('Welcome to my Encryptor')
msg=input('Enter the message to encrypt: ')

a,b=random.randint(1,p),random.randint(1,p)
print(f'(a, b) = ({a}, {b})')

enc1,enc2,enc3=[],[],[]
for c in msg:
    x=ord(c)
    enc1.append(( a*x + b) % p)
    enc2.append(( a*enc1[-1] + b) % p)
    enc3.append(( a*enc2[-1] + b) % p)
    
print(f'{enc1 = }\n{enc2 = }\n{enc3 = }')    
        
