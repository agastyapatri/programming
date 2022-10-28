"""
    Python Program to calculate the LCM of two numbers
"""
def LCM(num1, num2):
    greater = max(num1, num2)
    smaller = min(num1, num2)
    HCF = 0

    # Finding HCF
    for i in range(1, smaller+1):
        if(greater%i == 0) and (smaller%i == 0):
            HCF = i
    
    # Finding LCM
    if (num1%num2 == 0) and (num2%num1 == 0):
        return greater
    else: 
        return int((num1*num2)/HCF)

print("Enter the two numbers whose LCM is needed: ")
a = int(input())
b = int(input())

print(f"The LCM of {a} and {b} is: {LCM(a, b)}")


