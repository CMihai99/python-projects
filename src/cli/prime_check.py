# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

number = int(input("Enter number: "))

if number <= 1:
    print(f"Prime check: False. {number} is not a prime number")

else:
    for i in range(2, number):
        if (number % i) == 0:
            print(f"Prime check: False. {number} is not a prime number")
            break

    else:
        print(f"Prime check: True. {number} is a prime number")
