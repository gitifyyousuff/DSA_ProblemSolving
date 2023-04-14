#o(n)T|O(n)S
def caesarCipherEncryptor(string, key):
    newLetter = []
    newKey = key%26
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in string:
        newLetter.append(getNewLetter(i,newKey,alphabet))
    return "".join(newLetter)

def getNewLetter(newLetter,newKey,alphabet):
    newLet = alphabet.index(newLetter)+newKey
    return alphabet[newLet%26]


string = "xyz"
key = 2
caesarCipherEncryptor = caesarCipherEncryptor(string, key)
print(caesarCipherEncryptor)