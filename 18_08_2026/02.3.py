class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # reduce loops through the list once O(n), passing a (candidate, count) tuple taking O(1) space
        return __import__('functools').reduce(
            lambda acc, n: 
                # If count (acc[1]) is 0, make current 'n' the new candidate with a count of 1
                (n, 1) if acc[1] == 0 
                # Otherwise, keep the current candidate (acc[0]) and adjust count by +1 or -1
                else (acc[0], acc[1] + (1 if acc[0] == n else -1)), 
            
            nums,      # The array we are iterating over
            (None, 0)  # The starting state: candidate = None, count = 0
        )[0]           # '[0]' grabs just the winning candidate out of the final tuple to return it

# ==========================================
# Testing and Printing Logic
# ==========================================
if __name__ == "__main__":
    # 1. Create an instance of the Solution class
    solution = Solution()
    
    # 2. Define test arrays (using the examples from the problem)
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    
    # 3. Pass the elements to the function and print the results
    print(f"Input: {nums1}  -> Output: {solution.majorityElement(nums1)}")
    print(f"Input: {nums2}  -> Output: {solution.majorityElement(nums2)}")