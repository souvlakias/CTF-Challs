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

