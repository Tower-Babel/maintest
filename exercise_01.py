#exercise_01.py
#Alexander Palmer 1-3
#Ed Cruz 4-6
#Mahmoud Mohamed 7-9
#Brian Goldstein 10,2,5

#exercise 1
def grade_scale(x):
    if x >= 90:
        return "A"
    elif (x >= 80):
        return "B"
    elif (x >= 70):
        return "C"
    elif (x >= 60 ):
        return "D"
    else:
        return "F"   

x = int(input("Enter a grade from 0 to 100:")) 
print("Your grade is " + grade_scale(x))
#test
#print(grade_scale(61))         

#execrise 2 
#placed string in array and compared each array by index number
x = input("Enter a string")
y = input("Enter another string")

def string_input(x,y):
    x1 = len(x)
    y1 = len(y)
    
    for i in range(x1 and y1):
        if(x[x1-i-1] == y[y1-i-1]):
            return True
    return False   
print(string_input(x,y))      

#exercise 3

x = int(input("enter an integer greater than 1:"))
for i in range(x+1):
    print(x**2)

#exercise 10 wrong
words = input("Enter a string")
#new_word = words.split(" ")
new_word = []
for i in words:
    new_word.append(i)
print(new_word)

#exercise 10 correct
x = input("Enter a string: ")
y = list(x)
z = []
for i in range(0, len(y),3):
    a = []
    for k in range(0,3):
        if(i+k)< len(y):
            a.append(y[i+k])
    z.append(a)
print(z)            

#exercise 9
new_word = []
for i in range(1, 6):
    words = input("Enter a word:")
    new_word.append(words)

print(new_word)    
print("One String: "," ".join(new_word))

#exercise 6 incomplete
matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
r = int(input("enter a row num from 1 to 5: "))
c = int(input("enter a col num from 1 to 5: "))
matrix[r-1][c-1] = 1
for i in matrix:
    print(i)

#exercise 7
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

#EXERCISE 8

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

#exercise 4
 
n = int(input("Enter a number: "))
list1 = []
for i in range(n):
    list1.append(float(input("enter number: ")))
 
def Avg(list1):
    return sum(list1) / len(list1)
print(list1)
print(Avg(list1))

#exercise 5
 
list1 = []
list2 = []
for i in range(5):
    list1.append(int(input("enter a number for first list: ")))
for i in range(5):
    list2.append(int(input("enter a number for the second list: ")))
print("list 1: ")
print(list1)
print("list 2: ")
print(list2)
comList = set(list1).intersection(list2)
print("common values: ")
print(comList)