class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maximum= len(nums)/2
        for i in range(len(nums)-1):
            count= 1
            for j in range(i+1, len(nums)):
                if nums[i]== nums[j]:
                    count+= 1
            if count > maximum:
                return nums[i]
        