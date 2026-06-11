nums = [5, 6, 7, 1, 111, 9, 3, 4, 10, 70, 11, 1, 1, 5, 9]
x= 1

n= len(nums)
hash_map= {}

for i in range(0, n):
    hash_map= hash_map.get(nums[i], 0) + 1

print(f"the frq of numbers are : {hash_map}")
print(f"the frq of {x} is {hash_map.get(x, 0)}")

