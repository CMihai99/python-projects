# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

# Convert to binary
def decimalToBinary(n): 
	return bin(n).replace("0b","") 

# Run
if __name__ == '__main__': 
	print("Result:", decimalToBinary(int(input("Enter number: "))))
