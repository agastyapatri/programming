"""
    Calculate a factorial using recursion
"""

def factorial(integer):
    for i in range(1, integer+1):
        if i>1:
            result = i*factorial(i-1)
        else:
            result = 1
    return result


print("Enter a number whose factorial is needed: ")
n = int(input())
print(factorial(n))
