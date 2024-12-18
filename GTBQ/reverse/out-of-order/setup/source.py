from secret import FLAG
operations=[
    lambda x: x*2,
    lambda x: x+1,
    lambda x: x-4,
    lambda x: x^42
]
f=open('order.txt','r')

def enc1(msg:str):
    enc=[]
    for c in msg:
        c=ord(c)
        enc.append(operations[int(f.read(1))](c)) 
    return enc
def enc2(enc:list):
    enc2=[]
    for c in enc[::-1]:
        enc2.append(operations[::-1][int(f.read(1))](c))
    return enc2

if "__main__"==__name__:
    A=enc1(FLAG)
    B=enc2(A)
    print(B)