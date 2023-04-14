#o(n)T|O(n)S
def isPalindrome(string,i=0):
    j = len(string) - i-1
    return True if i>=j else string[i] == string[j] and isPalindrome(string,i+1)

    
string = "panbnap"
isPalindrome = isPalindrome(string)
print(isPalindrome)