fruits=('apple','banana','mango','grapes','orange')
print(fruits[1:3])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])
#count method
numbers=(1,2,3,2,1,2,5)
count_2=numbers.count(2)
print(count_2)

#Index method:
fruits=('pineapple','apple','banana','mango','apple')
index_apple=fruits.index('apple')
print(index_apple)


#Break:
for number in range(1,10):
    if number==6:
        print("Breaking the loop at number 5")
        break
    print("Number:",number)