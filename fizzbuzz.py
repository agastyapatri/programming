# Program to print "Fizz" if a number is divisible by 3 and "Buzz" if it is divisible by 5. "FizzbBuzz" if divisible by both.

def fizzbuzz(n):
    for i in range(1, n+1):
        if (i % 3 == 0 ) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0): print("Fizz")
        elif (i % 5 == 0): print("Buzz")
        else: print(i)






print("Enter a number: \n")
n = int(input())
fizzbuzz(n)
    




