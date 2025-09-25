# Functions
def greet():
    print("Welcome to python functions !")
    greet()

#Passing parameter and arguments
def greet_user(name):
    print("HELLO",name)
    greet_user("Rockstar")

#functions Arguments
def add (a,b):
    print("sum:",a+b)
    add(5,10)

#Key arguments
def indroduce(name,age):
    print(f'My name is {name}and I am {age}years old')
    indroduce(age=18,name="Rockstar")

# Default Arguments
def greet(name="Guest"):
    print("HELLO",name)
    greet()
    greet("Rockstar")