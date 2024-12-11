## Curve Tech Advent: Day 12

### Challenge

I recently encrypted a string *(your flag)* using the following Python code...

```Python
def encrypt(key, message):
    encrypted = ''
    for n in range(len(message)):
        encrypted += chr(ord(key[n]) + ord(message[n]))
    print(encrypted)
```

However, I lost the key!

Encrypted Message = ```¶ÍÔÚò²ç¶§e°```

Can you help me decrypt it? 
