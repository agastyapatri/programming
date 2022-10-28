"""
    Given a string s, find the first non repeating character and return its index. If it doesnt exist, return -1
"""

def firstuniquechar(string):
    hashmap = {} 
    
    # Populating a hashmap which has the counts of each char in the string.
    for char in string:
        if char not in hashmap: 
            hashmap[char] = 1
        else: 
            hashmap[char] += 1
    for i in hashmap:
        if hashmap[i] ==1: 
            return i
            
    #return hashmap 
    


print("Enter a string")
s = str(input())
print(firstuniquechar(s))


































