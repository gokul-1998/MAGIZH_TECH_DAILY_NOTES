# from typing import List
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return max(set(nums), key=nums.count)

nums=[2,2,3,9]    
print(max(set(nums), key=nums.count))
print(max(set(nums)))