#exercise_05
 
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