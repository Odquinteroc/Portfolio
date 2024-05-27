'''- Let’s say I give you a list saved in a variable: a = [[1, 4], [9, 16], [25, 36]]. Write one line of Python that takes this list a and makes a new list that contains [1, 4, 9, 16, 25, 36]'''
a = [[1, 4], [9, 16], [25, 36]]
# b= []
# for i in range(len(a)):
#     for j in a[i]:
#         b.append(j)

b = [item for sublist in a for item in sublist ]
print(b)