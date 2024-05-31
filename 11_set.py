#Set is an unordered collection of items.Every set elements is unique(no duplicates) and must be immutable(cannot be changed ).However, a set itself is mutable. We can add or remove items from it.

#Sets can also be used to perform mathematical set operations like union, intersection,symmetric difference etc.

#Characteristics:-
#Unordered
#Mutable
#No duplicates
#can't contain mutable data types

###CREATING A SET

##Empty set
s={}
print(s)
print(type(s))#it will show type as dictionary (as both set and dictionary share same syntax)

s=set()#this is the way to create a empty set 
print(s)
print(type(s))

##1D and 2D
s1={1,2,3}#1d set
print(s1)

#s2={1,2,3,{5,6}}
#print(s2) it will show error as set can't contain mutable data types(as 2d sets are not allowed)

##Hetrogeneous 
s3={1,4.5,'hello',True}
print(s3)#it will  show true in output as true =1 and in set there cannot be duplicate items

##Using type conversion 
s4=set([1,2,3,4])
print(s4)

##duplicates not allowed
s5={1,2,1,2,3,3}
print(s5)

##Set cannot have mutable items
#s6={1,2,3,[5,6]}
#print(s6)#it will show error as s6 is having list which is mutable

###ACCESSING ITEMS IN SET
#In sets accessing the items is  not allowed as if we want to access the items from set using indexing it will not work as items are unordered(index of any item is not fixed) that's why accessing the items is not allowed


###EDITING THE ITEMS
#in sets editing the items also not allowed with the same reason as accessing..


###ADDING THE ITEMS

##add(to add single item)
s={1,2,3,4}
s.add(5)#it will add an item in set(position will be decided by the system)
print(s)

##Update(to add multiple item)
s={1,2,3,4}
s.update([5,6,7])#it will update the items in set
print(s)

###DELETING THE ITEMS 

##del(to delete the complete set)
s={1,2,3,4}
del s
#print(s) it will show error as set is deleted now

##discard(to delete a particular item)
s={1,2,3,4}
s.discard(3)
print(s)
#if we want to delete an item which is not in set , it will not show any error

##remove(it is same as discard)
s={1,2,3,4}
s.remove(1)
print(s)

#if we want to delete an item which is not in set , it will show  error

##pop(it will delete the random item from set)
s={1,2,3,4}
s.pop()
print(s)
#we have no control over which item is going to be deleted

##clear(it will make the set empty by deleting every item in a set)
s={1,2,3,4}
s.clear()
print(s)


###OPERATIONS ON SET

s1={1,2,3,4,5}
s2={4,5,6,7,8}
##Union(|)
print(s1|s2)
#it will print the items only one item in case of duplicates

##Intersection(&)
#it will the common items 

print(s1&s2)

##Difference(-)
#it will print the items of s1 which is not in s2

print(s1-s2)

##Symmetric difference(^)
#it will print the items except common items

print(s1^s2)

##Membership test

print(1 in s1)
print(1 not in s2)

##Loops
for i in s1:
    print(i)


###SET FUNCTIONS