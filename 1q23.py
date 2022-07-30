# 23 Write a Python program to check whether a string starts with specified characters
def check(s, arr):
    result = []
    for i in arr:
       
        # for every character in char array
        # if it is present in string return true else false
        if i in s:
            result.append("True")
        else:
            result.append("False")
    return result
s= "sk9249758gmailcom"
arr = ['e', 'r', '1', '7']
print(check(s, arr))
