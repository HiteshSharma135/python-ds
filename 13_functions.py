#In Python, a function is a block of reusable code that performs a specific task. Functions help in organizing code, making it more readable and maintainable, and allowing for code reuse.

#Components of a Function
#Function Definition: Starts with the def keyword followed by the function name and parentheses (). Inside the parentheses, you can specify parameters.
#Function Body: The indented block of code that performs the function's task.
#Return Statement: Used to return a value from the function (optional)

def greet(name):
    """This function greets the person whose name is passed as a parameter."""
    return f"Hello, {name}!"

# Example usage:
print(greet("Alice"))  # Output: Hello, Alice!

#Types of Functions
#Built-in Functions: These are functions that are available in Python by default. Examples include print(), len(), type(), etc.

print("Hello, World!")  # Built-in function

#User-defined Functions: Functions that users create to perform specific tasks.

def add(a, b):
    return a + b


#Anonymous Functions (Lambda Functions): These are small, unnamed functions defined using the lambda keyword. They are often used for short, simple operations.

add = lambda x, y: x + y
print(add(2, 3))  
# Output: 5

#Recursive Functions: Functions that call themselves in order to solve a problem.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
 # Output: 120


 ###CREATING A FUNCTION

#function defination
def is_even(num):#here num is parameter
    """
    this is function which returns even or odd.
    it takes any valid integer
    """
    if num%2==0:
       return 'even' 
    else:
       return 'odd'
    
for i in range(1,11):
    x=is_even(i)#function calling
    #here i is argument
    print(x)

# in function , while creating a function value is passed -> parameter
#value passed while calling the function is -> argument

###TYPES OF ARGUMENT

##Default argument
#it is the default value of argument which is passed while creating a function to overcome the situation of error by other programmer 
#for ex:- if we are writing a code for power 
def power(a,b):
    return a**b

print(power(2,2))
#now we are giving the values to the function if in case any other person is using the function and he forgots to input the argument, in that case there will be error ... to overcome this situation we provide some default values to the function as in case any person does input the argument there will be no error...
def power1(a=1,b=1):
    return a**b

print(power1())#now if there is no value pass ,, there won't be any error

##Positional argument
#it is way in which python take its argument ... for ex:- position of a and b in def power(a,b) and value passed to it power(2,3) then there a=2 and b=3 its because of the position of the argument


##Keyword argument
#in case we donot know the position of the argument in that we can pass the value to the parameter by their name itself... example:-

print(power(b=5,a=4))

###  *args and *kwargs are the special Python keywords that are used to pass the variable length of arguments to a funciton.


##  *args
#it allows us to pass  a variable number of non-keyword arguments to a function.

#it is used in sitaution when we donot know that how many inputs are to passed to the function ,,, in that case we use args 

def multiply(*args):
#it stores the number of variable coming in tuple then perform the operation 
#here we can also use any name other than args it will work the same just put the * sign before that
    product=1

    for i in args:
        product=product*i

    return product

ans=multiply(1,2,4,5,6,7,4)
print(ans)

#to find the documentation of any function just type function.__doc__ and print it 

## **kwargs
#it allows us to pass any number of keyword arguments
#keyword arguments mean that they contain a key-value pair like dictionary

#if we want any thing to print in key value pairs in any number then we use **kwargs it takes input in dictionary format

#if we wan to  print country with their capital

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,'->',value)

display(india='delhi',bangladesh='dhaka',USA='washington')

#any name can be use in place of kwargs it will work

#POINTS TO REMEMBER 
#order of arguments matter(normal->*args->**kwargs) 


###HOW FUNCTION ARE EXECUTED IN MEMORY?

##Steps of Function Execution in Memory
#Function Definition:

#When a function is defined, Python creates a function object. This object contains the function’s code, the default values of parameters (if any), and other metadata.
#The function name is stored in the current namespace, pointing to the function object.

def my_function(x, y):
    return x + y
#Function Call:

#When a function is called, Python allocates a new stack frame for that function call. The stack frame is a data structure that contains information needed to execute the function.
#This stack frame includes:
#Local variables and arguments
#A reference to the function object
#The return address (the point in the code where the function was called)
#The previous stack frame (for nested or recursive calls)

result = my_function(5, 3)
#Argument Passing:

#The arguments provided in the function call are assigned to the function's parameters in the new stack frame.
#If *args or **kwargs are used, they are converted to a tuple and a dictionary, respectively.

#Execution:

#Python begins executing the function’s code line by line.
#Local variables are created in the stack frame. If the function accesses global variables, it refers to the global namespace.
#Python maintains a call stack to keep track of active stack frames. The current function's stack frame is at the top of the call stack.
#Return Statement:

#When the function encounters a return statement, it returns the specified value to the caller.
#The stack frame for the function call is removed (popped) from the call stack, freeing up memory.
#Execution resumes at the point where the function was called, using the return value.
               

###WITHOUT RETURN
#if a function does not have return then python send return statement as none

def is_even(num):
    if num%2==0:
        print('even')
    else:
        print('odd')

print(is_even(7))#here as there is no return statement so by default return-> none as it displays none ... when we print(is_even(7))

L=[1,2,3,4]
print(L.append(5))#it will print none as l.append is not list ,,it is returning none value
print(L)#now it will print the list

###VARIABLE SCOPE 
# SEE SESSION 6 OF CAMPUSX FROM 1:01HR

###NESTED FUNCTIONS
#use python tutor to see the visualisation of the program

def f():
    def g():
        print('inside g')
    g()
    print('inside f')


f()

#here if we call g() from the main function then it will show error as nested function is hidden from the main function ...as it cannot access the g()


##programs of nested function

def g(x):
    def h():
        x='abc'
    x=x+1
    print('in g(x):x=',x)
    h()
    return x

x=3
z=g(x)


