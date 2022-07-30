#16.Write a Python function to insert a string in the middle of a string. Sample function and result :insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
my_string = 'Hello, what are doing'
split_strings = my_string.split()
split_strings.insert(3, 'you')
final_string = ' '.join(split_strings)
print(final_string)
