#exercise_04
 
n = int(input("Enter a number: "))
list1 = []
for i in range(n):
    list1.append(float(input("enter number: ")))
 
def Avg(list1):
    return sum(list1) / len(list1)
print(list1)
print(Avg(list1))
