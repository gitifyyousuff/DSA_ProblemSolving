#o(n)T|O(n)S
def isPalindrome(string):
   reversed_chars = []
   for i in reversed(range(len(string))):
       reversed_chars.append(string[i])
   return "".join(reversed_chars) == string

string = "panbdnap"
isPalindrome = isPalindrome(string)
print(isPalindrome)
