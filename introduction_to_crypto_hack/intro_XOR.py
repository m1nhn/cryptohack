from Crypto.Util.number import *


a = 'label'
b = 13

a_bytes = a.encode('utf-8')

b_bytes = long_to_bytes(b,len(a_bytes))

c_bytes = bytes([x^y for x,y in zip(a_bytes, b_bytes)])

c = bytes_to_long(c_bytes)

print(c_bytes)

# from pwn import *
# print(xor(b'label',13))