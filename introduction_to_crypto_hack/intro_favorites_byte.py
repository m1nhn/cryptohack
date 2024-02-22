encrypted_hex = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

# Convert hex string to bytes
encrypted_bytes = bytes.fromhex(encrypted_hex)

# Iterate through possible keys (single bytes)
for key in range(256):
    # XOR each byte with the current key
    decrypted_bytes = bytes(x ^ key for x in encrypted_bytes)
    
    # Check if the result looks like plausible ASCII text
    if all(32 <= byte <= 126 or byte == 10 or byte == 13 for byte in decrypted_bytes):
        # Convert to string for easier checking
        decrypted_string = decrypted_bytes.decode('utf-8')
        
        # Print the potential result along with the key
        #print(f"Key: {hex(key)}, Decrypted: {decrypted_string}")
        
        # Check if the word 'crypto' is present in the decrypted string
        if 'crypto' in decrypted_string:
            print("Word 'crypto' found. Stopping the loop.")
            print(f"Key: {hex(key)}, Decrypted: {decrypted_string}")
            break
