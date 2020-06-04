"""
Goal is to write a python function to sort the words in string

input: String of words separated by spaces

Output: String of words sorted aplhabetically, also have to take care of case sensitive.
"""

words = input("Enter the list of words separeated by spaces: ").split(" ")

# converting the words in lower and appending with original word to take care of case sensitive words
words = [w.lower() + w for w in words]
words.sort()
# removing the extra added words for getting back the original String

words = [w[len(w)//2:] for w in words]
print(words)
