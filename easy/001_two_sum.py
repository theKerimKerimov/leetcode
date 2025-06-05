from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1, num_1 in enumerate(nums):
            for index_2, num_2 in enumerate(nums):
                if num_1 + num_2 == target and index_1 != index_2:
                    return [index_1, index_2] 

nums = Solution()     
print(nums.twoSum([2,7,11,15], 9)) 
print(nums.twoSum([3,2,4], 6)) 
print(nums.twoSum([3,3], 6)) 
