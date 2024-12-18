rev_operations=[
    lambda x: x//2,
    lambda x: x-1,
    lambda x: x+4,
    lambda x: x^42
]
def dec2(enc:list,order:str):
    i=0
    dec2=[]
    for c in enc:
        dec2.append(rev_operations[::-1][int(order[i])](c))
        i+=1
    return dec2[::-1]

def dec1(enc:list,order:str):
    i=0
    dec1=[]
    for c in enc:
        dec1.append(rev_operations[int(order[i])](c))
        i+=1
    return dec1

enc2=[117, 109, 221, 46, 107, 176, 43, 115, 94, 106, 113, 48, 57, 92, 50, 89, 220, 136, 49, 220, 158, 134, 169, 134]
order=open('order.txt','r').read()[:len(enc2)*2]
order1=order[:len(enc2)]
order2=order[len(enc2):]
enc1=dec2(enc2,order2)
FLAG=dec1(enc1,order1)
print(bytes(FLAG).decode())


