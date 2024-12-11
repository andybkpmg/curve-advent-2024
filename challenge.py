message=""
key=""

def encrypt(key, message):
    encrypted = ''
    for n in range(len(message)):
        encrypted += chr(ord(key[n]) + ord(message[n]))
    return encrypted

encrypted = encrypt(key, message)
print(encrypted)