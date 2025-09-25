import array
nums=array.array('i',[1,2,3,4])

# INSERT AT SPECIFIC INDEX
nums.insert(1,10)
print(nums)

# REMOVING ELEMENT
nums.remove(10)
print(nums)

#REMOVE ELEMENTS BY INDEX
del nums[0]
print(nums)

#BASIC OPERATIONS OF ARRAY
print(len(nums))
print(sum(nums))
print(max(nums))
print(min(nums))
