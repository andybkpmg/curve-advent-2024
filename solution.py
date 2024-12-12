# def decrypt(key, message):
#     decrypted = ''
#     for n in range(len(message)):
#         try:
#             decrypted += chr(ord(message[n]) - ord(key[n]))
#         except ValueError:
#             return 'invalid key'
#     return decrypted

encrypted = '¶ÍÔÚò²ç¶§e°'

with open('./keys.txt', 'r') as f:
    for key in f.read().split('\n'):
        if (len(key) > len(encrypted)):
            decrypted = ''
            for n in range(len(encrypted)):
                try:
                    decrypted += chr(ord(encrypted[n]) - ord(key[n]))
                except ValueError:
                    continue
                except IndexError:
                    continue
            if decrypted.startswith('flag{') and decrypted.endswith('}'):
                print(f'Key: {key} - Message: {decrypted}')