#exercise_07
# Create two empty lists to hold data.
list_all = []
list_even = []

# Get user input.
# Validate input and add numbers to the first list.
user_input = ''
while user_input != 'QUIT':
    user_input = input('Enter a number or QUIT to quit: ')
    if user_input != 'QUIT':
        list_all.append(int(user_input))

# Add even numbers to the second list.
for even in list_all:
    if even % 2 == 0:
        list_even.append(even)

# Display both lists.   
print('All nums: ', list_all)   
print('Even: ', list_even)  
