def square(x):
    return x*x
numbers=[12,13,14,154,16,17,18,19]
squared=list(map(square,numbers))
print(squared)

# Filters Examples
def is_even(x):
    return x%2==0
numbers=[1,2,3,4,5,6,7,8,9]
even_numbers=list(filter(is_even,numbers))
print(even_numbers)

#Reduce() Examples
from functools import reduce
def add(x,y):
    return x+y
numbers=[1,2,3,4,5,6]
sum_numbers=reduce(add,numbers)
print(sum_numbers)
