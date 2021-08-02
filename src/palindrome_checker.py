'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''

def isPalindrome(s):
	return s == s[::-1]

s = input("Enter word: ")
ans = isPalindrome(s)

if ans:
	print("Word is a palindrome")
else:
	print("Word isn't a palindrome")
