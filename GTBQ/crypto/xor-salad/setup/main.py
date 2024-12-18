from Crypto.Util.number import bytes_to_long as b2l
from secret import FLAG
FLAG=b2l(FLAG)

A = b2l('🥒🥒🥒🥒🥒🥒🥒🥒🥒🥒🥒🥒🥒🥒🥒🥒'.encode())

B = A ^ b2l('🧅🧅🧅🧅🧅🧅🧅🧅🧅🧅🧅🧅🧅🧅🧅🧅'.encode()) ^ b2l('🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅'.encode())

C = B ^ b2l('🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋'.encode())

print(A ^ B ^ C ^ FLAG)