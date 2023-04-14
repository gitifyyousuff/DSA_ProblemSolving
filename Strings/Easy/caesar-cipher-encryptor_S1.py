#o(n)T|O(n)S
def caesarCipherEncryptor(string, key):
    newLetter = []
    newKey = key %26
    for letter in string:
        newLetter.append(getNewLetter(letter,newKey))
    return "".join(newLetter)

def getNewLetter(letter,newKey):
    newLetterCode = ord(letter)+newKey
    return chr(newLetterCode) if newLetterCode <=122 else chr(96+newLetterCode%122)


string = "xyz"
key = 2
caesarCipherEncryptor = caesarCipherEncryptor(string, key)
print(caesarCipherEncryptor)