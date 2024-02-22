from pwn import *

encrypted_mess = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
encrypted_mess = bytes.fromhex(encrypted_mess)

key = b'myXORkey'

xored = xor(encrypted_mess,key)
print(xored)
