"""
    Python Program to sort an array in ascending order 
"""

def sortarray(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            temp = arr[i]
            if(arr[i] > arr[j]):
                arr[i] = arr[j]
                arr[j] = temp 

    return arr






print(sortarray([4,5,7,8,34,2,1,4,6,7]))
print(sortarray([8,7,6,5,4,3,2,1,1]))

