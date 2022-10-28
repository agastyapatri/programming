"""
    Python program to segregate the 0s and 1s in an array. 
    Ex: Input = [0,1,0,0,1,1,1,0,0,0]
        Output = [0,0,0,0,0,0,1,1,1,1]
"""

def segregate(array):
    count = 0
    for i in range(len(array)):
        if array[i] == 1: 
            array[i] = 0
            count += 1

    for i in range(count):
        array[-(i+1)] = 1

    return array
        

print(segregate([0,1,0,0,1,1,1,0,0,0]))




