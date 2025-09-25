# Handling Zero division Error
try:
    x=10/0
except ZeroDivisionError:
    print("x cannot divide by zero")
finally:
    print("program ended")


# Example:2
try:
    num=int("abc")
    result=10/0
except ValueError:
    print("X invalid number")
except ZeroDivisionError:
    print("X cannot divide by zero")
finally:
    print(" Done")


#Example 3
try:
    f=open("data.txt")
except Exception as e:
    print("Error:",e)
finally:
    print("File handling attempted")