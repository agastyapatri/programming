"""
   Given two strings a and b, return True if b is an anagram of a and False otherwise 
"""

def anagram(string1, string2):
   return (len(string1) == len(string2) and (set(string1) == set(string2)) )


print("Enter the first string: ")
a = str(input())
print("Enter the second string: ")
b = str(input())
print(anagram(a, b))







