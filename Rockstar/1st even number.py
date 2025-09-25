numbers=(1,3,5,7,9,2)
for num in numbers:
    if num % 2==0:
        print("First even number found:",num)
        break
    print(num)
else:
    print("No even number found")