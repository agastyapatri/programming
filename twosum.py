"""
    Given an array of integers, return the indices of the two numbers such that they add up to a specific target.
"""


def twosum(array, target):
    #   Iterate through the array
    #   find complement of each element
    #   check if complement is present in array 
    ans = []
    for i in range(len(array)):
        complement = target - array[i]
        if complement in array:
            ans.append((i, array.index(complement)))
            break 

    return ans 


    



print(twosum([2,7,11,15], 18))
print(twosum([6,7,10,11,12,13], 13))

