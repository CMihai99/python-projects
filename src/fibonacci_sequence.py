'''
Developed by: Calinescu Mihai
Date: 18 Mar, 2021

Github: https://github.com/CMihai99
'''


# Calculate sequence
def fibonacci(n):
    # Declare variables
    a = 0
    b = 1
    
    # Initialize sequence
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

fibonacci(int(input("Enter number: ")))
