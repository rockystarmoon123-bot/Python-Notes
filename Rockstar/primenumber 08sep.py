num=int(input("Enter a Number: "))
count=0
for i in  range (1,num+1):
    if (num%i==0):
        count +=1
if(count==2):
    print("The given number is a prime number")
else:
    print("The given number is not a prime number")