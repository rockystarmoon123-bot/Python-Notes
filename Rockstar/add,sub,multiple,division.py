num1=float(input("Enter first number:"))
operation=input("enter operation(+,-,*,/):")
num2=float(input("Enter second number:"))
if operation  =="+":
    print("result","=" ,num1+num2)
elif operation =="-":
    print("result","=",num1-num2)
elif operation =="*":
    print("result","=",num1*num2)
else:
    if operation == "/":
        print("result","=",num1/num2)