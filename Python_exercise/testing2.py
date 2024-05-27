a = [[1,2], [3,4],[5,6]]
# [1,2,3,4,5,6]

b =[item for sublist in a for item in sublist]
print(b)
