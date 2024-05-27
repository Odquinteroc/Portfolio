'''- Given a dictionary my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}. Write code to print out a list of sorted key based on their value. For example, in this case, the code should print out ['b', 'd', 'a', 'c']'''

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
'''a = []
for i in my_dict:
    a.append(i)
print'''

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
sorted_keys = sorted(my_dict, key=my_dict.get)
print(sorted_keys)