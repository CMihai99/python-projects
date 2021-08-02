'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


numbers = int(input("Enter a number: "))

if numbers<=1:
    print(numbers, "is not prime")

else:
    for i in range(2, numbers):
        if (numbers%i)==0:
            print(numbers, "is not prime")
            break
    else:
        print(numbers, "is prime")
