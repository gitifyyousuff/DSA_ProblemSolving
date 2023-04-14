#O(m+n)
def generateDocument(characters, document):
    flag_char = False
    character_list = list(characters)
    if len(document) == 0:
        flag_char = True
    if len(document) <= len(characters) :
        for char in document:
            if char in character_list:
                flag_char = True
                character_list.remove(char)
            else:
                flag_char = False
                break
    return flag_char


characters =  "aheaolabbhb"
document =  "hello"

generateDocument = generateDocument(characters, document)
print(generateDocument)