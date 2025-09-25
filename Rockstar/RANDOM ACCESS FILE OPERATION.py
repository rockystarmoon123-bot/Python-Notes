f=open("data.txt","r")
print(f.read(7))
print("pointer at :",f.tell())
f.seek(0)
print(f.read(10))
f.close