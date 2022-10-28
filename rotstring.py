"""
    Verifying if two given strings are mututally rotational. 
    Example: str1 = "AgastyaPatri", str2 = "styaPatriAga"
    ans: Yes

    Example: str1 = "aabbccdd", str2 = "ddccbbaa"
    ans: No 
"""

def rotstrings(str1, str2):
    string1 = list(str1)
    if len(str1) != len(str2):
        return f"Strings {str1} and {str2} are not equal!"
    
    #   rotating a string and checking if it is equal to the second string. 
    for i in string1:
        string1.remove(i)
        string1.append(i)
        if "".join(string1) == str2:
            return True
        
    return False
      




print(rotstrings("AgastyaPatri", "styaPatriAga"))
print(rotstrings("aabbccdd", "ddccbbaa"))




