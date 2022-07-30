# 12. Write a Python program to count the occurrences of each word in a given sentence.
def occurance_of_word(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(occurance_of_word('honesty is best policy'))
