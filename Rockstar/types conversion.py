#1. LIST =>TUPLE
my_list=[1,2,3,4]
my_tuple=tuple(my_list)
print(my_tuple)
print(type(my_tuple))

#2.TUPLE => LIST
mytuple=(5,6,7,)
mylist=list(mytuple)
print(mytuple)
print(type(mylist))

#3.LIST=>SET
mylist=[1,2,3,3,4,4,5]
myset=set(mylist)
print(myset)
print(type(myset))

#4.SET=>LIST
myset={10,20,30}
mylist=list(myset)
print(mylist)

#5.DICTIONARY => LIST OF KEY
student={"Name":"JOHN","age": 20,"Grade": 'A'}
keyslist=list(student.keys())
print(keyslist)

#6.DICTIONARY => LIST OF VALUES
student={'NAME':"JOHN",'AGE':20,'GRADE': "A"}
valueslist=list(student.values())
print(valueslist)

#7.DICTIONARY => LIST OF ITEMS
student={'NAME':"JOHN",'AGE':20,'GRADE': "A"}
itemslist=list(student.items())
print(itemslist)