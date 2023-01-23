word = input("Enter a string: ")
x = ""
y = ""
for i in word:
    if i.isupper():
        x+= i
    elif i.islower():
        y+= i
        
result = y + x

