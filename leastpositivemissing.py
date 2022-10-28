"""
    Python code to find the least positive number missing from an array of integers.
    Example:    Input = [1, -5, 7, -2, -3, 0, 10, 100, 3 ]
    Ans: 2
"""


def leastpositive(array):
    ans = 0
    smallest = min(array)
    largest = max(array)
    
    for i in range(0, largest+1):
        if i not in array:
            ans = i
            break 


    return ans


print(leastpositive([1, -5, 7, -2, -3, 0, 10, 100, 3 ]))
    
