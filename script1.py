#exercise 1
def get_unique_list(my_list):
   
    unique_list = []


    for i in my_list:
        if i not in unique_list:
            unique_list.append(i)


    return (unique_list)




   
my_list =[1,2,3,2,1,4]      
unique_list = get_unique_list(my_list)
print(unique_list)


