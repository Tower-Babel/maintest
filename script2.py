#exercise 2
def get_combined_dict(my_dict_1, my_dict_2):

    new_dict = {}

    for x, y in my_dict_1.items():

        if (x in my_dict_2.keys()):

            new_dict[x] = y + my_dict_2[x]

    return new_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
