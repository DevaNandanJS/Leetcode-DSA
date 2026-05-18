nums = [5, 6, 7, 1, 111, 9, 3, 4, 10, 70, 11, 1, 1, 5, 9]
x= 1

frq= {}

for i in range(0, len(nums)):
    if nums[i] in frq:
        frq[nums[i]] += 1
    else:
        frq[nums[i]] = 1

print(f"the frequency of all numbers in the array is: {frq}")
print(f"frequency of {x} is {frq[x]}")


