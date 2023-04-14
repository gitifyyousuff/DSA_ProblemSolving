def firstNonRepeatingCharacter(string):
    indx_flg = False
    lst_string = list(string)
    for i in lst_string :
        lst_string.remove(i)
        if i in lst_string :
            continue
        else:
            return string.index(i)

    # if indx_flg:
    #     return -1
    
string = "faadabcbbebd"
# string = "fad"
firstNonRepeatingCharacter = firstNonRepeatingCharacter(string)
print(firstNonRepeatingCharacter)