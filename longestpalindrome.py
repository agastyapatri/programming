"""
    Given a string s, return the longest palindroming substring in s. 
    Example: aaabbaa
    return: aabbaa

    Example 2: babad
    return: bab

    Example 3: cbbd 
    return: bb
"""

def longestpalindrome(string):
    

    substrings = [] 
    palindrome_strings = [] 
    
    #   finding the palindromic substrings    
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            s = string[i:j]
            if( s == s[::-1]): palindrome_strings.append(s)
    
    #   how to find what the substrings are 
    palindrome_strings = list(set(palindrome_strings)) 

    #   how to find the longest of them 
    longest = 0
    longest_palindrome = None 
    for string in palindrome_strings:
        if len(string) > longest:
            longest = len(string)
            longest_palindrome = string
     
    return longest_palindrome

print(longestpalindrome("aaabbaa"))
print(longestpalindrome("babad"))
print(longestpalindrome("cbbd"))



