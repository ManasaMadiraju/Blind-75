from ast import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else: 
            return True
        
# simplified version
# return len(set(nums)) < len(nums)
        
# Time Complexity: O(n)
# Space Complexity: O(n)