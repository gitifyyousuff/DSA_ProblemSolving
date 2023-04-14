#o(n^2)T|O(n)S
def isPalindrome(string):
   reversed_string = ''
   for i in reversed(range(len(string))):
       reversed_string+=string[i]
   return reversed_string == string

    
    
string = "panbdnap"
isPalindrome = isPalindrome(string)
print(isPalindrome)