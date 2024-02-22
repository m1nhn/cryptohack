from pwn import *
from Crypto.Util.number import *


KEY1 = int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313', 16)
result_xor = int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', 16)

KEY2 = KEY1 ^ result_xor

result_xor_3 = int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', 16)

key3 =  KEY2 ^ result_xor_3

result_xor_flag = int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf',16)

flag = result_xor_flag ^ KEY1 ^ KEY2 ^ key3

flag = str(hex(flag)[2:])

print("Your flag is : " + str(bytes.fromhex(flag)))

print(str(bytes.fromhex(flag)))

#print(hex(flag)[2:])