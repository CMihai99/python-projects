# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 5th, 2021

for fizzbuzz in range(int(input("Range: "))):
    # Multiples of both 3 and 5 print "fizzbuzz"
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue

    # Multiples of 3 print "fizz"
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue

    # Multiples of 5 print "buzz"
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue

    print(fizzbuzz)
