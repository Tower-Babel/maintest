#exercise_08

# Create two empty Lists.
original = []
non_repeated = []

# Get user imput for the list.
for i in range(10):
    print ('Enter number',i+1,':')
    num = int(input())
    original.append(num)

# Add numbers that appear only once to the non_repeated list.
non_repeated = [i for i in original if original.count(i)==1]

# Display both lists.
print('Original list: ', original)
print('Nums that appear once: ', non_repeated)
