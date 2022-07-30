# 19.Write a Python program to get the last part of a string before a specified character
str = 'this is my first experiment'
print(str.rsplit('/', 1)[0])
print(str.rsplit('-', 1)[0])
