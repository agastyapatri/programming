"""
    Given an array arr of N integers, write a function that returns true if there is a triplet that satisfies a^2 + b^2 = c^2
"""

def pythagoreantriplet(array):
    state = False

    #   Sorting the array in O(n^2)
    for i in range(len(array)):
        for j in range(len(array)):
            temp = array[i]
            if (array[i] > array[j]): 
                array[i] = array[j]
                array[j] = temp 

    #   Iterating through the array to find corresponding pythagorean elements with the initial element as the hypotenuse
    for h in array:
        h_sq = h**2
        for a in range(1, h+1):
            a_sq = a*a
            for b in range(1, h+1 ):
                b_sq = b*b
                if(h_sq == a_sq + b_sq):
                    if( (a in array) and (b in array)):
                        state = True
                    else:
                        state = False
    return state 
    





# Done in O(n^3)
print(pythagoreantriplet([3,2,4,5,6]))
print(pythagoreantriplet([3,8,5]))




