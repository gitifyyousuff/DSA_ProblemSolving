 
def findThreeLargestNumbers(array):
    threeLargest = [None,None,None]
    for num in array:
        updateLargest(threeLargest,num)
    return threeLargest

def updateLargest(threeLargest,num):
    if threeLargest[2] is None or num>threeLargest[2]:
        shiftUpdate(threeLargest,num,2)
    elif threeLargest[1] is None or num>threeLargest[1]:
        shiftUpdate(threeLargest,num,1)
    elif threeLargest[0] is None or num>threeLargest[0]:
        shiftUpdate(threeLargest,num,0)

def shiftUpdate(threeLargest,num,idx):
    for i in range(idx+1):
        if i == idx:
            threeLargest[i] = num
        else:
            threeLargest[i] = threeLargest[i+1]
    
