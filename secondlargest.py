"""
    Program to find the second largest element of an array 
"""


def secondlargest(array):
    
    #   Finding the maximum of the array
    largest = 0
    for i in range(len(array)):
        if (array[i] > largest): largest = array[i]
        else: continue
    array.remove(largest)

    secondlargest = 0
    for i in range(len(array)):
        if (array[i] > secondlargest): secondlargest = array[i]
        else: continue

    return secondlargest 
    

   
    






print(secondlargest([5,67,8,2,3,5,7,78,3,2,1,2,3,45,6,6]))
print(secondlargest([4,5,7,7,7,5,4,2,2,2,555,32,1,13,4,6,7,6]))
