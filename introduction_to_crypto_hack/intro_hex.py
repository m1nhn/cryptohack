a = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
b = 'crypto{You_will_be_working_with_hex_strings_a_lot}'
print(bytes.fromhex(a)) #Convert from hex to string
print(bytes(b, 'utf-8').hex()) #Convert from string to hex with utf-8 format