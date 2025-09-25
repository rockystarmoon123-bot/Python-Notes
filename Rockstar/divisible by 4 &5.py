num=int(input("Enter a number"))
if num %4 ==0 and  num %5==0:
    print(num,"is divisible by both 4 and 5")
elif num% 4 == 0:
    print(num,"is divisible by 4")
elif num % 5 ==0:
    print(num,"is divisible by 5")
else:
    print(num,"is not divisible by both 4 and 5")