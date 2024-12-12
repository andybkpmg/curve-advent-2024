# Solution

## Finding the KEY

Firstly, we obtained a list of commonly used passwords/keys. This can be found in keys.txt. There's only 1000 in this list but lets assume our key is somewhere in this list.

If we look at the code used to encrypt, it is simply swapping characters out. We can therefore assume that the decrypted message is the same length of the encrypted string.

If we next look at the logic for iterating the message and key characters you can determine that the key must also be at least as long or longer than the original message.

```Python
for n in range(len(message)):
```
> **_INFO:_**  Function usage [len](https://docs.python.org/3/library/functions.html#len), [range](https://docs.python.org/2/library/functions.html#range)

We can therefore disreguard any keys in the list that aren't long enough giving us a much shorter keys list.

```Python
encrypted = '¶ÍÔÚò²ç¶§e°'
keys = []

# open the gile containing the lis tog keys
with open('./keys.txt', 'r') as f:
    # for each key
    for key in f.read().split('\n'):
        # is the key longer than the encrypted string
        if (len(key) > len(encrypted)):
            # yes, store the key
            keys.append(key)

# This will give us a list of X possible keys.
print(keys)
```

## Encryption

Next we need to look at the logic used for obfuscating the characters. If you're familiar with [unicode](https://en.wikipedia.org/wiki/List_of_Unicode_characters) it will help. Basically unicode is a universally recognised list of every character which is assigned an identifying corresponding numerical value.

We will need to understand how the functions used work with unicode.

* The [ord()](https://docs.python.org/3/library/functions.html#ord) function gives you the integer that represents the unicode character.

* The [chr()](https://docs.python.org/3/library/functions.html#chr) function converts an integer to the mapped unicode character.

When "encrypting", the unicode integer for each character in both the key and the message are added togeather. This new value is then used to idenitfy the new obsfoscated unicode character.

```Python
for n in range(len(message)):
    encrypted += chr(ord(key[n]) + ord(message[n]))
```

Example: The unicode integer for ```X``` *(our message)* is 88. The unicode integer for ```y``` *(our key)* is 121.

88 + 121 = 209 - The unicode character for 209 is ```Ñ``` *(our obsfoscated character)* so we replace ```X``` with ```Ñ```.

## Decryption

To reverse this "encryption" method, all we need to do is reverse the character calculation. i.e. Instead of adding the values togeather, we subtract them.

```Python
for n in range(len(message)):
    decrypted += chr(ord(message[n]) - ord(key[n]))
```

If we iterate the list of potential keys we identified earlier and test them in this code against our encrypted message we will see possible decrypted strings.

**_Note:_** *If we use the wrong key, the integer used to identify the unicode characters will be incorrect or invalid so the output will make no sense.*

## Solution

Here is the complete solution.

```Python
# our encrypted message
encrypted = '¶ÍÔÚò²ç¶§e°'

# read the keys file
with open('/keys.txt', 'r') as f:
    # for each key in the file
    for key in f.read().split('\n'):
        # is the key long enough?
        if (len(key) > len(encrypted)):
            # try to decrypt the message using the key
            decrypted = ''
            # for each character in the encrypted message
            for n in range(len(encrypted)):
                try:
                    # reverse the encryption logic
                    decrypted += chr(ord(encrypted[n]) - ord(key[n]))
                # possibly the unicode char doesn't exists, skip
                except ValueError:
                    continue
                except IndexError:
                    continue
            # lets assume the message was a flag
            if decrypted.startswith('flag') and decrypted.endswith('}'):
                print(f'Key: {key} - Message: {decrypted}')

> Key: Password12345 - Message: flag{CuRv3}
```

...and there we have it. We have performed a [brute-force](https://doubleoctopus.com/security-wiki/threats-and-tools/brute-force-attack/) decryption process against an encrypted string and successfully unscrambled the message using common keys.

## Learnings

### Brute-Force will always succeed

Nothing is 100% secure. Given enough time and computing power, a brute-force attack will ultimately always successfully guess your password/key.

The biggest difference you can make to the time this takes is the length. Using a basic computer it would only take 30 minutes to successfully guess a random 8 character password such as ```hkdUebfg```. However, ```hkxcdUedwbfg``` would take 2 millenums to guess!

| | 8 Characters | 10 Characters | 12 Characters |
| - | - | - | - |
| Lower Case | Instantly | Instantly | Weeks |
| 1 Upper Case Character | 30 minutes | 1 Month | 5 Years |
| 1 UC + 1 Number | 1 Hour | 6 Years | 2000 Years |
| 1 UC + 1 Num + Symbol | 1 Day | 50 Years | 63,000 Years |

### Quantum computing

Quantum computing will make all current encryption null and void. Estimates indicate that the computational power of quantum computers qubits will mean that currently secure 2048 bit RSA keys will take 5-8 hours to crack.

### Obsfoscation is not encryption

When encrypting sensitive information, we should use larger keys and much more sophisticated cryptographic methods that can utilise complex algorithms such as AES or RSA etc...

### Choose hard to guess keys

Billions of real passwords have been leaked online over the last decade and [analysis](https://www.researchgate.net/publication/327623664_Analysis_of_Publicly_Leaked_Credentials_and_the_Long_Story_of_Password_Re-use) of their complexity is alarming. 

Check if your password has already been leaked? https://haveibeenpwned.com/Passwords