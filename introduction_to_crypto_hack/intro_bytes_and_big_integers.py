#Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

#The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

from Crypto.Util.number import *

mess = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

bytes_mess = long_to_bytes(mess)

print(bytes_mess)