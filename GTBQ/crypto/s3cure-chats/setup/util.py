from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long as b2l,long_to_bytes as l2b
import os

FLAG='.........GTBQ{d0n7_u53_5m4ll_3xp0n3n7_6uy5}..........'
def make_key(N_len=1024,e=65537):
    key = RSA.generate(N_len,e=e)
    return key

def enc_message(message:str,key:RSA.RsaKey):
    n=key.n
    e=key.e
    msg=b2l(message.encode())
    return pow(msg,e,n)

def dec_message(c:int,key:RSA.RsaKey):
    n=key.n
    d=key.d
    return l2b(pow(c,d,n)).decode()


messages:list[(str,str)]=[('Bob','Hey guys!, i made a new chat app that we can use to chat securely even if it\'s public.'),
         ('Alice','That\'s cool! How does it work?'),
         ('Bob','It basically encrypts a message using the public key of the recipient, and only the recipient can decrypt it using their private key.'),
         ('Bob','So just go to the secrets page, select who you are sending to and type your message. The app will do the encryption/decryption for you!'),
         ('Bob','Alice check it out, im sending you a very important secret!'),
         ('Eve','No fair, tell me as well!'),
         ('Emily','I\'here tooo!'),
         ('Bob','Ok ok, i\'m sending you all the secret message!. I just hope you didn\'t do anything stupid with your public keys 😛')
       ]

                             
                             

users:dict[str,RSA.RsaKey]={
    'Bob':make_key(),   
    'Alice':make_key(e=3),
    'Eve':make_key(e=3),
    'Emily':make_key(e=3),
}

secret_messages:list[(str,str,int)]=[('Bob','Alice',enc_message(FLAG,users['Alice'])),
                             ('Bob','Eve',enc_message(FLAG,users['Eve'])),
                             ('Bob','Emily',enc_message(FLAG,users['Emily']) )
]



def add_user(username:str,key:RSA.RsaKey):
    users[username]=key 
    os.system(f'cp ./static/avatars/guest.png ./static/avatars/{username}.png')
    messages.append(('Bob',f'Welcome \'{username}\' to the chat!, i will send you an example encrypted message, that only you can read!'))
    secret_messages.append(('Bob',username,enc_message(f'hey there {username}😛',key))
    )
