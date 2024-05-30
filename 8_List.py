#list in python 
#lists is datatype where you can store multiple items under 1 name.More technically , lists act like dynamic arrays which means you can add more items on the go.

##Arrays vs Lists
#fixed vs dynamic size
#homogeneous(in arrays we need to store only similar type of data) vs hetrogeneous(in list we can store different datatypes under 1 name)
#speed of execution is more in array 
#arrays are memory efficient in comparision to lists


##how lists are stored in memory
#lists are stored in memory in referential array format

#to see the address of any item we use id func

L=[1,2,3]
print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))


