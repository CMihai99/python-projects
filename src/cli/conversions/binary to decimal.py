'''
Developed by: Calinescu Mihai
Date: 17 Mar, 2021

Github: https://github.com/CMihai99
'''


# 1. Convert to decimal
def binaryToDecimal(n): 
    return int(n,2)

# 1. Run Program
if __name__ == '__main__': 
    print("Result:", binaryToDecimal(input("Enter number: ")))