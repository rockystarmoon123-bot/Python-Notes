num=int(input("Enter a Number: ")) #num=13
count=0
for i in  range (1,num+1):
    if (num%i==0):#13%1==0,13%2==0,13%3==0,13%13==0
        count +=1 #count=1, count=2

if(count==2):
    print("The given number is a prime number")
else:
    print("The given number is not a prime number")