import random

number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# Original list
print(number_list)
# Output [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# List after first shuffle
random.shuffle(number_list)
print(number_list)
# Output [42, 28, 14, 21, 7, 35, 49, 63, 56, 70]

# List after second shuffle
random.shuffle(number_list)
print(number_list)
# Output [14, 21, 70, 28, 49, 35, 56, 7, 42, 63]
 Run
