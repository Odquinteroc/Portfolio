myStr = 'Python Strings'
print(myStr)
print(myStr[0])
print(myStr[3:7])
print(myStr[4:])
print(myStr*3)
print(myStr+" is Powerfull")

print("Updated String:" , myStr[:6] + 'String')
print("Updated String:\a" , myStr[:6] + 'String')
print("Updated String:\b" , myStr[:6] + 'String')
print("Updated String:\n" , myStr[:6] + 'String')
print("Updated String:\t" , myStr[:6] + 'String')

# %s string
# %d integer
# %f float
# %  tuple of number of digit

print ("My name is %s and I am %d years old!" % ('Oscar', 27)) # prints out My name is Jack and #I am 33 years old 

myList = [ 'Monday', 26 , 2024, 'is', 'sunny' ]
mySubList = ['date', 0]
print (myList)	# Prints complete list
print (myList [0])	# Prints first element of the list
print (myList [2:4])	# Prints elements starting from 2nd till 3rd
print (myList [3:])	# Prints elements starting from 3rd element
print (mySubList * 2) # Prints list two times
print (myList + mySubList) # Prints concatenated lists

myList [4]= 'rainy'
print ('print an updated list', myList)

#Len
print(len(myList))

#max & min
# print(max(myList)) 
#print(min(myList))

'''there is an error because myList has string object and the max and min function just work with integer and float
'''

#append
myList.append('Hola')
print(myList)

#count
print(myList.count('Monday'))

#extend
myList.extend(mySubList)
print(myList)

#index
print(myList.index('Monday'))

#insert
myList.insert(0,'hola')
print(myList)

#pop
thislist = myList.copy()
thislist.pop()
print(thislist)

#remove
thislist.remove('date')
print(thislist)

#reverse
thislist.reverse()
print(thislist)

#sort   
thislist.sort()
print(thislist)


