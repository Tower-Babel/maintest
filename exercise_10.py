#exercise_10
#Alexander Palmer 1-3
#Ed Cruz 4-6
#Mahmoud Mohamed 7-9
#Brian Goldstein 10,2,5 


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