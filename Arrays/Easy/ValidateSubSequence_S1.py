# O(n) T| O(1)S
def isValidSubsequence(array, sequence):
    arrayIdx = 0
    seqIdx = 0
    while arrayIdx < len(array) and seqIdx < len(sequence):
        if sequence[seqIdx] == array[arrayIdx]:
            seqIdx += 1
        arrayIdx += 1
    return seqIdx == len(sequence) 

array =  [5, 1, 22, 25, 6, -1, 8, 10]
sequence =  [1, 6, -1, 10]
isValidSubsequence = isValidSubsequence(array, sequence)
print(isValidSubsequence)