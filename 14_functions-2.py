###FUNCTIONS ARE 1ST CLASS CITIZENS

##type and id 
#function in python is acts as data type

def square(num):
    return num**2

#same as any other datatype we can check the datatype and id of any function
print(type(square))
print(id(square))

##reassign
#we can reassign the function to any other variable

x=square
print(id(x))

##deleting a function 
#we can also delete the function as it acts like an datatype

del square
#now if want to access the square() then it will show error

##Storing
def square(num):
    return num**2

#we can store the function as any other data type 

L=[1,2,3,square]
print(L[-1])
print(L[-1](5))

##Returning a function 

def f():
    def x(a,b):
        return a+b
    return x

val=f()(3,4)
print(val)

#in this program firstly 42 f call and it ignore and it return the x which is another function in f() then ,,, val=x(3,4) and it return a+b and val =7
#in this program a function is returning another function ,, due to which we can access the inner /nested function 
#use python tutor for this code

##Function as argument

def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_b')
    return z()

print(func_b(func_a))


###LAMBDA FUNCTION 
#A lambda function is small anonymous function
# A lambda function can take any number of arguments , but only have one expression.

#Syntax
lambda a,b:a+b#a,b -> parameters ,,, a+b->expression

#lambda function to square 

a= lambda x:x**2
print(a(2))

#lambda function to add two numbers

a=lambda x,y:x+y
print(a(8,5))

##Difference between lambda function vs normal function
#NO name
#lambda has no return value (infact, returns a function)
#written in 1 line
#not reusable 

#they are used with HOF(HIGHER ORDER FUNCTION )

#check if string has 'a'

a=lambda s:'a' in s
print(a('hello'))

#odd or even

a=lambda num:num%2==0
print(a(4))
#another way with if else

a=lambda x:'even' if x%2==0 else 'odd'
print(a(5))


###HIGHER ORDER FUNCTION 
#a function which returns the function or a function  which take another function as it input

#example
#function which takes a list as input and gives it square as output

def square(x):
    return x**2

def transform(f,L):
    output=[]
    for i in L:
        output.append(f(i))

    print(output)

L=[1,2,3,4,5]

transform(square,L)#this transform is HOF 

##map
#it accept an lambda function and list
#with the help of this , we can make logic in list

#function to square the elements of list items using map
a=list(map(lambda x:x**2,[1,2,3,4,5]))
print(a)


#odd even labelling of list items
L=[1,2,3,4,5]
a=list(map(lambda x:'even' if x%2==0 else 'odd',L))
print(a)

#fetch names from a list of dictionary 

users=[
    {
        'name':'rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'hitesh',
        'age':21,
        'gender':'male'
    },
    {
        'name':'isha',
        'age':18,
        'gender':'Female'
    }
]

a=list(map(lambda users:users['gender'],users))
print(a)


###FILTER
#it takes lambda function and list

#number greater than 5

L=[3,5,6,4,2]
a=list(filter(lambda x:x>5,L))
print(a)

#fetch fruits starting with 'a'

L=['apple','banana','avacado','guava']

a=list(filter(lambda x:x.startswith('a'),L))
print(a)

##Reduce
#to use it we need to import a module called functools

#sum of all items
import functools
a=functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
print(a)

#find minimum

a=functools.reduce(lambda x,y:x if x<y else y,[11,22,12,98] )
print(a)