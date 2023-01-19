#execrise_02 
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
