# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

number = int(input("Enter number: "))

if number <= 1:
    print("Prime check: False.", number, "is not prime")

else:
    for i in range(2, number):
        if (number % i) == 0:
            print("Prime check: False.", number, "is not prime")
            break

    else:
        print("Prime check: True.", number, "is prime")
