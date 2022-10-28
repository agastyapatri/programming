"""
    Python program to reverse a string 
    3 methods identified:
        1. using "".join()
        2. creating a new string and adding. (similar to 1)
        3. Vi
"""

def revstring(string):
    return "".join([string[-(i+1)] for  i in range(len(string))])
print(revstring("aaabbbcccddd"))
print(revstring("AgastyaPatri"))

