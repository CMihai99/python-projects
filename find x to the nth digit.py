'''
Developed by: Calinescu Mihai
Date: 21 Mar, 2021

Github: https://github.com/CMihai99
'''


import math

# Count number
def count_number(number):
    counter = 0
    counter_number = number
    while counter_number > 0:
        counter_number //= 10
        counter += 1
    return counter

# Select digit
def digit_selector(number, selected_digit, total):
    total_counter = total
    calculated_select = total_counter - selected_digit
    number_selected = int(number / math.pow(10, calculated_select))
    while number_selected > 10:
        number_selected -= 10
    return number_selected

def main():
    x = int(input("Find: "))
    n = int(input("to the ?th digit: "))
    total_digits = count_number(x)                # Count total digits of x
    select_n = digit_selector(x, n, total_digits) # Select ?Th's digit
    if total_digits < n: # if total_digits is smaller than n, print error
        print("Error. Number is too high")
    else:
        print("Result:", select_n)

# Run program
if __name__ == '__main__':
    main()