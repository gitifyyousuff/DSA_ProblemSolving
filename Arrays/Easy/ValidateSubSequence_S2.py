# O(n) T| O(1)S
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

#input data given below
array =  [5, 1, 22, 25, 6, -1, 8, 10]
sequence =  [1, 6, -1, 18]
isValidSubsequence = isValidSubsequence(array, sequence)
print(isValidSubsequence)