"""
    Given a valid IP address, return its defanged version, where every dot is surrounded by [].
    Example: 127.0.0.1
    Output: 127[.]0[.]0[.]1
"""

def defang(IP):
    ans = ""
    for i in IP:
        if i == ".": 
            ans += "["
            ans += i
            ans += "]"
        else: ans += i
    return ans 






print("Enter the IP address to be defanged: ")
ip = str(input())
print(defang(ip))





