#O(n)T|(On)S
def moveElementToEnd(array, toMove):
    a,b =[],[]
    for i in array:
        if i != toMove:
            a.append(i)
        else:
            b.append(i)
    c = a+b
    return c
        
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove= 2
moveElementToEnd = moveElementToEnd(array, toMove)
print(moveElementToEnd )