x = [0.0, 3.0, 5.0, 2.5, 3.7] 	#define an arra
print(type(x))

#print x
print("Originally x = ",x)

#remove the third element
x.pop(2)			#pop off based on the index
print(x)

#remove the element equal to 2.5
x.remove(2.5)			#remove based on the value of the element
print(x)

#add an element at the end
x.append(1.2)
print(x)

#get a copy
y = x.copy() 			#we can avoid changing y by using copy
print(y)

#how many elements equal 0.0
print(y.count(0.0)) 	#lists have a built in count, count will return the num of times that the number shows in list

#print the index with a value 3.7
print(y.index(3.7))		#if there is an element of y that has 3.7 it will tell index of the value

#sort the list
y[0]=5.9				#will sort in place
print(y)
y.sort()
print(y)

#reverse sort
y.reverse()				#will reverse sort
print(y)

#remove all elements
y.clear()
print(y)