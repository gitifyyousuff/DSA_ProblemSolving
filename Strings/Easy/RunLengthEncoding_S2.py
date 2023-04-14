#O(n)TS
def runLengthEncoding(string):
    list_string = []
    count = 1
    for i in range(1,len(string)):
        cur_occur = string[i]
        prev_occur = string[i-1]
        if cur_occur != prev_occur or count==9:
            list_string.append(str(count))
            list_string.append(prev_occur)
            count = 0
            
        count +=1
    list_string.append(str(count))
    list_string.append(string[len(string)-1])
        
    return "".join(list_string)

string = "AAAAAAAAAAAAABBCCCCDD"
runLengthEncoding = runLengthEncoding(string)
print(runLengthEncoding)