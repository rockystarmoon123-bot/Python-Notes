num1=int(input("Enter first integer:"))
num2=int(input("Enter second integer:"))

#Bitwise AND
bitwise_and=num1&num2

#Bitwise OR
bitwise_or=num1|num2

# Bitwise XOR
bitwise_xor = num1 ^ num2

# Bitwise NOT
bitwise_not_num1 = ~num1
bitwise_not_num2 = ~num2

#Bitwise Left shift
left_shift = num1 << 1

#Bitwise right shift
right_shift = num2 >> 2

print(f"\n Bitwise AND of {num1} @ {num2} = {bitwise_and}")
print(f"\n Bitwise OR of {num1} | {num2} = {bitwise_or}")
print(f"\n Bitwise NOT of {num1}  = {bitwise_not_num1}")
print(f"\n Bitwise NOT of  {num2} = {bitwise_not_num2}")
print(f"\n Bitwise XOR of {num1} ^ {num2} = {bitwise_xor}")
print(f"\n Bitwise left shift of {num1} << 1 = {left_shift}")
print(f"\n Bitwise right shift of {num2} >> 2= {right_shift}")
#output
# Enter first integer:7
# Enter second integer:5
# Bitwise AND of 7 @ 5 = 5
# Bitwise OR of 7 | 5 = 7
# Bitwise NOT of 7  = -8
# Bitwise NOT of  5 = -6
# Bitwise XOR of 7 ^ 5 = 2
# Bitwise left shift of 7 << 1 = 14
# Bitwise right shift of 5 >> 2= 1
