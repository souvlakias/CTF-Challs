from json import loads,dumps
from base64 import b64encode,b64decode,b32encode,b32decode
from zlib import compress,decompress
from requests import get

def make_cookie(data:dict)->str:
    return compress(b32encode(b64encode(dumps(data).encode().hex().encode()))).hex()

def parse_cookie(cookie:str)->dict:
    return loads(bytes.fromhex(b64decode(b32decode(decompress(bytes.fromhex(cookie))).decode()).decode()).decode())

def is_admin(cookie:str)->bool:
    return parse_cookie(cookie)['admin']

def safe_input(input:str)->bool:
    return not '1337' in input and not '1337' in get(input,allow_redirects=False).url

print(make_cookie({'admin':True}))