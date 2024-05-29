#this is first class of python 1 

###1. Python output 
#python is case sensitive language
print("hello world")
print(7)
print(8.55)
print(True)
#we can print any type of data in a single print function 
print("hello",1,2.55,True)
#print gives the result by giving space in every type of data 
print("hello",1,2.55,True,sep='-')
# to overwrite the behaviour of print function of providing space by every data ,,, we use sep='' and can put any character whatever we want after every data see line 12
print('hiii')
print('hitesh')
#if we use two print function one after another in different line than it automatically separate the given data in nextline 
print('hello',end='-')
print('india')
#to overcome the default behaviour of print function , use end... see line 16-18



###2.Datatypes

#Integer data type
print(7)
#python can support integer data upto 1*10^308
print(1e308)


#Float/Decimal
print(5.25)
#python can support float data upto 1.7*10^308


#Boolean (we don't use '' while printing boolean values)
print(True)
print(False)


#Text/String
print('Hello world')

#complex number
print(4+5j)

#List (it is like array but have some different features)
print([1,2,3,4,5])

#Tuple (same as list just use () instead of [])
print((1,2,3,4,5,6))

#Sets 
print({1,2,3,4,5})

#Dictionary (it is in key value pairs)
print({'name':'hitesh','gender':'male'})


###3. type function 
#type function is used to detect the type of data

print(type(2))
print(type(5+5j))
type(2.5)
type(True)
type('hello')


###4 Variables (it is container where values are stored )

# python we dont need to tell the data type this is called dynamic typing 
# in c/c++ we need to tell the data type this is called static typing
#Dynamic Binding (it is concept where type of data is not fixed everytime we enter different value according to it it will change its datatype) see 74
a=5
print(a)
a='hitesh'
print(a)
#here datatype of a is not fixed

#static binding (it is concept where variable cannot chnage its datatype once it is declare like in c/c++ )  


#creating multiple variables 
a,b,c=1,2,3
print(a,b,c)

#to provide constant value
a=b=c=5
print(a,b,c)


### 5. Keywords and identifiers

#keyword (we cannot use keyword as variable name)
#In Python, an identifier is a name used to identify variables, functions, #classes, modules, or any other object. Identifiers must follow certain rules:
#a.They can contain letters (both uppercase and lowercase), digits, and underscores.
#b.They must start with a letter (a-z, A-Z) or an underscore (_).
#c.They cannot start with a digit (0-9).
#d.They are case-sensitive (for example, myVar, MyVar, and MYVAR are all different #identifiers).
#e.They cannot be a reserved word or keyword.


###6. User input

#to take input from user we use input function
#print(input('enter your name'))

a=(input("enter value of a"))
b=(input("enter value of b"))
result = a + b
print(result)
#it is showing as adding string this is because it is taking input as string not as integer to overcome this we need to convert the type of string to int

a1=int(input("enter the value of a"))
b1=int(input("enter the value of b"))
result1=a1+b1
print(result1)

### 7. Type conversion (it is way of converting the type of datatype)
# implicit type conversion it is automatically done by the compiler 
#example
a=4
b='hitesh'
print(5+5.6)
print(type(5),type(5.6))
#it automatically detects the type of datatype

#explicit (we need to convert the datatype explicitly)
#str to int
print(int('5'))

#int to str
print(str(5))

#float
float(4)


###8. Literals (value which is being stored in variable is literal)

a=0b1010 #binary literal
b=100 #decimal literal
c=0o310 #octal literal
d=0x12c #hexadecimal literal

#float literal
float_1=10.5
float_2=1.5e2
float_3=1.5e-3

#complex literal
x=3.14j

print(a,b,c,d)
print(float_3)
print(x,x.real,x.imag) #x.real is used to print only real part of complex  number and x.imag is used to access only imaginaty part 

#String literal

string='this is python'
string1="this is hitesh"
char="h"
multiline_str="""it is used to print multiline string """
unicode=u"\U0001F60A"
raw_str=r"raw \n string"

print(string)
print(string1)
print(unicode)
print(raw_str)  


#boolean literal
a=True+4
b=False-5
print("a:",a)
print("b:",b)
#we can perform mathematical operation on boolean values as python take true as 1 and false as 0

#None literal
# as we know we cannot declare variables in python to overcome this problem we can declare any variable as none
a=None 