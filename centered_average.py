"""
    Return the centered average of an array of ints. This is equal to the mean average value of a list of numbers, excluding the largest and the smallest values of the array
"""

def centered_average(array):
    summation = 0
    temp = 0
    
    #   Sorting the arrays
    for i in range(len(array)):
        for j in range(i , len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    
    #   performing the sum
    smallest = array[0]
    largest = array[-1]

    for i in array[1 : -1]:
        summation += i

    return int(summation / len(array[1:-1])) 

print(centered_average([1,2,3,4,100]))
print(centered_average([1,1,5,5,10,8,7]))
print(centered_average([-10,-4,-2,-4-2,0]))





