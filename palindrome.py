"""
    Python Program to check if a string is a palindrome or not
"""

def palindrome(string):
    ans = ""
    for char in string:
        if char.isalpha(): ans += char.lower()
    return (ans == ans[::-1])



print("Enter a string: ")
s = str(input())
print(palindrome(s))


