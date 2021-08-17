# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 17th, 2021

paragraph = input("Enter paragraph: ")

split_paragraph = len(paragraph.split('.'))

if split_paragraph <= 1:
    print(f"Number of sentences in the paragraph: {str(split_paragraph)}")

elif split_paragraph > 1:
    print(f"Number of sentences in the paragraph: {str(split_paragraph)}")
