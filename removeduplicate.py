"""
    Python Program to remove the duplicates in an array
"""

def removeduplicates(array):
    ans = [] 
    for num in array:
        if num not in ans:
            ans.append(num)

    return ans



print(removeduplicates([112,3,1,3,5,5,5,122,5,55,5,5,12,4,6,7,8,3,2,1,3,3,3,3]))
print(removeduplicates([1,1,1,1,1,1,1,2,3,4,5,6,6,6,6,6,7,8,8,9,9,9,10]))




