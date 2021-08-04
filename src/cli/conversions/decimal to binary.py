'''
Developed by: Calinescu Mihai
Date: 17 Mar, 2021

Github: https://github.com/CMihai99
'''


# 1. Convert to binary
def decimalToBinary(n): 
	return bin(n).replace("0b","") 

# 2. Run Program
if __name__ == '__main__': 
	print("Result:", decimalToBinary(int(input("Enter number: "))))
