# 8.  Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def longest_word_in_list(my_list):
   max_length = len(my_list[0])
   temp = my_list[0]

   for element in my_list:
      if(len(element) > max_length):

         max_length = len(element)
         temp = element
   return max_length

my_list = ["ram", "shyam", "radha", "Exercises"]
print("The list is :")
print(my_list)
print("The result is :")
print(longest_word_in_list(my_list))
