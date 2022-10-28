"""
    You are climbing a staircase, it takes n steps to reach to the top. Each time you can climb
    or two steps. In how many distinct ways can you climb to the top.
"""

def climbingstairs(n):
    #   Finding prime factors of the number in terms of 1 and 2.
    t1 = 0 
    t2 = 1
    fib = 0
    for i in range(0, n):
        fib = t1 + t2 
        t1 = t2
        t2 = fib
    return fib 
    



print((climbingstairs(1)))
print(climbingstairs(2))
print(climbingstairs(3))
print(climbingstairs(5))












