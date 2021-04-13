'''
Developed by: Calinescu Mihai
Year: 2021

Github: https://github.com/CMihai99
'''


for fizzbuzz in range(int(input("Max Range: "))):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0: # Check fizzbuzz
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)