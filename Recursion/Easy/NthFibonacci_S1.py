#Naive approach
#O(2^n)T|O(n)S
def getNthFib(n):
    if n==2:
        return 1
    elif n==1:
        return 0
    else:
        return getNthFib(n-1)+getNthFib(n-2)
    

n = 15
getNthFib = getNthFib(n)
print(getNthFib)
