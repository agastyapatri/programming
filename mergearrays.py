"""
    Python program to merge two arrays. 
"""

def mergearrays(arr1, arr2):
    ans = []
    for i in range(len(arr1) + len(arr2)):
        if i < len(arr1): ans.append(arr1[i])
        else: ans.append(arr2[i - len(arr1)])
        
    
    return ans


print(mergearrays([1,2,3,4,5,6], [7,8,9,10]))
print(mergearrays([5,6,7,4,2,5,7], [23,4,5,7,1]))




