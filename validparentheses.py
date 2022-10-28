"""
    Program to check if the complement of the parentheses is present in a given string 
"""

def validparentheses(string):
    state = False
    
    hashmap = {"(" : ")", "[" : "]", "{" : "}"}
    
    for i in string:
        if i in hashmap:
            if hashmap[i] in string: state = True 
    return state 
            



print("Enter a string: ")
s = str(input())
print(validparentheses(s))




