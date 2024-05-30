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



##LIST COMPREHENSION