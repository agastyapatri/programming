"""
    Python Program to count the number of characters in a given string in O(n) time complexity
"""

def countchars(string):
    count = 0
    for i in string:
        count += 1

    return count


print(countchars("abasrbcoreejk"))
print(countchars("aasfgsadfaaf"))
print(countchars("akdsfyaydsfffff"))





