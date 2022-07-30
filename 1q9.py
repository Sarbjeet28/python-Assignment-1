# 9.Write a Python program to remove the nth index character from a nonempty string. """
string=input("Enter the string:")
n=int(input("Enter the index of the character to remove:"))
first = string[:n]   
last = string[n+1:]  
print("Modified string:",first+last)
