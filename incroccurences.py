"""
    Python program to print numbers of an array in increasing order of their occurences. 
"""

def incrocc(array):
    hashmap = {}
    for i in array:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    for i in hashmap:
        if hashmap[i] == max(list(hashmap.values())):
            print(hashmap[i])
            hashmap[i] = 0
            
        

    return hashmap 


print(incrocc([1,2,2,1,3,3,3]))























