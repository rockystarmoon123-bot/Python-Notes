# 1st Question Answer
num1 = int(input("enter your 1st number: "))
num2 = int(input("enter your 2nd number: "))
def mul(a,b):
    print("Multiplication of a and b is:",a*b)
mul(num1,num2)

# 2nd Question Answer
num = int(input("enter your number: "))
def numbers(x):
    if num%2==0:
        print("even")
    else:
        print("odd")
numbers(num)

# 3rd Question Answer
num=int(input("enter number:"))
def factorial(n):
    result = 1
    for i in range(1,n+1):
         result *= i
    return result
print(factorial(num))

#4th Question and Answer
num1 = int(input("enter your 1st number:"))
num2 = int(input("enter your 2nd number:"))
num3 = int(input("enter your 3rd number:"))
def number(a,b,c):
    if num1<=num2<=num3 or num2<=num1<=num3:
        print("Largest of three numbers is:",num3)
    elif num2<=num3<=num1 or num3<=num2<=num1:
        print("Largest of three numbers is:",num1)
    else:
        print("Largest of three numbers is:",num2)
number(num1,num2,num3)
# 5th Question Answer
word=input("your word:")
def reverse_string(S):
    return S [::-1]
print(reverse_string(word))
# 6th Questions answer
word=input("Enter your name:")
def count_vowels(word):
    vowels="aeioAEIOU"
    count=0
    for char in word:
        if char in vowels:
            count+=1
    return count
print(count_vowels(word))