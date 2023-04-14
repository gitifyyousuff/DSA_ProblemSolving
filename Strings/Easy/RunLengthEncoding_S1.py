def runLengthEncoding(string):
    nw_string = ""
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1] and count<9:
            count+=1
        else:
            nw_string += str(count)+string[i]
            count = 1

    nw_string += str(count)+string[-1]
    return nw_string       



string = "AAABBCD"
runLengthEncoding = runLengthEncoding(string)
print(runLengthEncoding)