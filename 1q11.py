# 11. Write a Python program to remove the characters which have odd index values of a given string.
c = input("enter the string")

temp = ""

for i in range(len(c)):

    if i%2!=0:

        temp = temp+c[i]

print(temp)
