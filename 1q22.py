#22 Write a Python program to remove a newline in Python. 
list1 = ["Starbucks\n", "has the \nbest", "coffee\n\n "]
rez = []

for x in list1:
    rez.append(x.replace("\n", ""))

print("New list : " + str(rez))
