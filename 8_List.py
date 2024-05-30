#list in python 
#lists is datatype where you can store multiple items under 1 name.More technically , lists act like dynamic arrays which means you can add more items on the go.

###Arrays vs Lists
#fixed vs dynamic size
#homogeneous(in arrays we need to store only similar type of data) vs hetrogeneous(in list we can store different datatypes under 1 name)
#speed of execution is more in array 
#arrays are memory efficient in comparision to lists


###how lists are stored in memory
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


###Characteristics of lists

##ordered 
#l is not equal to l1 as there ordering is not same
L=[1,2,3]
L1=[3,2,1]
L==L1

##changable/mutuable
#lists are mutuable 

##hetrogeneous(it can store different types of data types under same name)

name=[1,'true','hitesh',5.3]

##items can be duplicate
L=[1,1,2,3]

##lists are dynamic(size is not fixed)

##nested lists are allowed

L=[1,2,['hitesh',7,8]]

##items can be accessed
#it can be done using indexing or slicing



##can contain any type of objects in python 


###CREATING A LIST

##Empty list 
print([])

##1D list

print([1,2,3,4,5])

##2D list
print([1,2,3,[4,5]])

##3D list

print([[[1,2],[3,4]],[[5,6],[7,8]]])

##Hetrogeneous list

print([1,True,5.6,5+6j,'hello'])

##using type conversion
#it just convert every character of string into a list format
print(list('hello'))


###ACCESSING ITEMS FROM A LIST

##Indexing

L=[1,2,3,4,5]
#positive indexing(it starts from left to right and initial value is 0)
print(L[0])

#negative indexing(it starts from right to left and initial value starts from-1 )
print(L[-1])

#in indexing if we want to access any item index which is not in the list it will show error

#accessing elements from 2d list

L=[1,2,3,[4,5]]
#accessing 4
print(L[3][0])#positive indexing
print(L[-1][-2])#negative indexing

#accessing elements from 3d list
L=[[[1,2],[3,4]],[[5,6],[7,8]]]
#accessing 5
print(L[1][0][0])
#accessing 3
print(L[0][1][0])


##Slicing 
#it is used when we need to extract multiple items from the list 

L=[1,2,3,4,5]

print(L[0:3])#last number is not included
print(L[0:])#to print the entire list
print(L[-4:-1])#last number is not included
print(L[:-1])#to print the entire list
print(L[0::2])#to skip the alternate number in list till end 
print(L[::-1])#to reverse the list
#it is same concept we read in strings 



###ADDING ITEMS TO LIST

##Apend
#if we want to add a single item at the end of list ,, in that case we use append
L=[1,2,3]
L.append(6)
print(L)

#special result
L.append([8,9])#it will add as single item in a list
print(L)

##Extend
#to add multiple items in a list at the end of list
L=[1,2,3]
L.extend([4,5,6])
print(L)

#special result
L.extend('delhi')#it will break string into single words then add to the list
print(L)
 

##Insert
#to add the item in a list in between the list 
#it takes input as location(where we want to add the item) and the new item(which is to be added)
L=[1,2,3]
L.insert(1,100)
print(L)


###EDITING ITEMS IN A LIST

L=[1,2,3,4,5]
#we want to change 5->500 using indexing
L[4]=500
#we can use slicing in editing
L[1:4]=[100,200,300]
print(L)


###DELETING ITEMS IN A LIST

##del
L=[1,2,3,4,5]
print(L)
del L
#print(L)#it will now show error as list is deleted now

L=[1,2,3,4,5]
#to delete any particular item
#using indexing
del L[-1]#to delete last item

#using slicing
del L[1:3]
print(L)

##remove
#to remove/ delete any particular item or number without knowing its indexing
#in this index position is not required just delete the particular  number
L=[1,2,3,4,5,6]
L.remove(5)
print(L)


##pop
#if we donot pass the index in pop func it remove the last item of list as it behaviour

L=[1,2,3,8,9]
L.pop()#it will remove the last item in list
print(L)

L.pop(1)#it will remove the item at index value 1
print(L)


##clear
#to clear every item from the list it is used
#it makes the list empty

L=[1,2,3]
L.clear()
print(L)



###OPERATIONS ON LIST 

##Arithmetic(+,*)
L1=[1,2,3,4,5]
L2=[6,7,8,9]

print(L1+L2)
#it just merge the list by using + operator

print(L1*3)#it just repeat the L1 list three times and then merge it 

##Membership(in/not in)

L1=[1,2,3,4,5]
L2=[1,2,3,[4,5]]
print(5 in L1)#it will check that 5 present in L1 list or not
print(5 in L2)#it will check in 2d list, as gives false result ... as 5 is not present in L2 as an individual but in a another list

##loops

L1=[1,2,3,4,5]
L2=[1,2,3,[4,5]]

for i in L2:
    print(i)


###List Functions

##len/min/max/sorted

L=[2,1,5,7,0]

#len function is used to find the length of list (number of items in a list)
print(len(L))

#min function is used to find the minimum number from the list
#it will work on the homogeneous list only otherwise it will show error
print(min(L))

#max function is used to find the maximum number from the list
print(max(L))

#sorted function is used to sort the list items in ascending order
print(sorted(L))
#to sort in descending order
print(sorted(L,reverse=True))


##Count
#this function is used to count the frequency of items in a list
L=[1,1,2,3,4,2,3,3,3,4]
print(L.count(1))
print(L.count(15))


##Index
#this functio is used to find the index of any item in a list
#if a number occurs more than a time in a list then it will tell about the first occurence index of that item
L=[1,1,2,3,4,2,3,3,3,4]
print(L.index(3))


##Reverse
#it is used to reverse the list items
#it permanently reverses the list items 

L=[2,1,5,0,7,8]
print(L.reverse())


##Sort vs Sorted
#sort is similar as sorted 
#sort permanently sort the list items unlike sorted
L=[2,1,5,0,7,8]
print(L.sort())

##Copy 
#it just creates the copy of list with different address
#it make shallow copy
L=[2,1,5,0,7,8]
print(L)
print(id(L))
L1=L.copy()
print(L1)
print(id(L1))
#just see the address of both the L1 and L after copy as they are different




