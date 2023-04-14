#O(nlogn)T|O(1)S
def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if coin>change+1:
            return change+1
        change +=coin
    return change+1

coins = [5, 7, 1, 1, 2, 3, 22]
# coins = [1,1,3]
coins_sol = nonConstructibleChange(coins)
print(coins_sol)