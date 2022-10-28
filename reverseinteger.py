"""
    Given a signed integer x, return x with its digits reversed. 
    Example: stdin : 1200, stdout: 21
"""


def reverseinteger(n):
    """
        takes the number, converts to string, reverses the string, returns the ans 
    """
    target = str(n)
    return int("".join(target[::-1]))
        

print("Enter the integer to be reversed: ")

n = int(input())
print(reverseinteger(n))

























