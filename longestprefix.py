"""
    Python program to find the longest common prefix amongst a list of strings
"""

def longestcommonprefix(strings):
    
    prefix = "" 
    hashmap = {}
    for string in strings:
        for i in range(len(string)):
            if string[i] not in hashmap:
                hashmap[string[i]] = 1
            else:
                hashmap[string[i]] += 1
    
    for letter in hashmap: 
        if hashmap[letter] == len(strings):
            prefix += letter
    return hashmap




print(longestcommonprefix(["flower","flow","flight"]))
print(longestcommonprefix(["dog","racecar","car"]))


