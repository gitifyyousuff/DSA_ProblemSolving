#Memoization or HashTable approach
#O(n)T|O(n)S
def getNthFib(n,memoize={1:0,2:1}):
    if n in memoize:
        return memoize.get(n)
    else:
        memoize[n]= getNthFib(n-1,memoize)+getNthFib(n-2,memoize)
        return memoize.get(n)


n = 12
getNthFib = getNthFib(n)
print(getNthFib)
