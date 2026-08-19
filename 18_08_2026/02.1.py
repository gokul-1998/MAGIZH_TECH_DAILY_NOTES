class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


# [2,2,2,2,3,4,4] # 7/2=3.5=>4
# [2,2,2,2,2,2,3,3,4,4]

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# [2,2,2,3,4,4] # 6/2=3
