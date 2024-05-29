'''- Given a dictionary my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}. Write code to print out a list of sorted key based on their value. For example, in this case, the code should print out ['b', 'd', 'a', 'c']'''

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
'''a = []
for i in my_dict:
    a.append(i)
print'''

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
sorted_keys = sorted(my_dict, key=my_dict.get)
print(sorted_keys)

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
sorted_keys = [key for value, key in sorted(zip(my_dict.values(), my_dict.keys()))]
print(sorted_keys)

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
sorted_keys = sorted(my_dict.keys(), key=lambda k: my_dict[k])
print(sorted_keys)

from operator import itemgetter

my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
sorted_keys = [k for k, v in sorted(my_dict.items(), key=itemgetter(1))]
print(sorted_keys)

