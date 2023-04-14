#Iterative approach
#O(n)T|O(1)S
def getNthFib(n):
    if n == 1:
        return 0
    elif n ==2:
        return 1
    counter = 3
    n1,n2=0,1
    while counter<=n:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        counter += 1
    return n3


n = 12
getNthFib = getNthFib(n)
print(getNthFib)
