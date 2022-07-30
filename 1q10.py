# 10.Write a Python program to change a given string to a new string where the first and last chars have been exchanged. """
text = input('Enter a string: ')
newtext = text[-1]+text[1:-1]+text[0]
print('New string:', newtext)
