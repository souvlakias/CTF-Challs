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

# [117, 109, 221, 46, 107, 176, 43, 115, 94, 106, 113, 48, 57, 92, 50, 89, 220, 136, 49, 220, 158, 134, 169, 134]