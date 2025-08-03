from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_num = float('inf')

        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest_num):
                closest_num = nums[i]


            elif abs(nums[i]) == abs(closest_num):
                closest_num = max(nums[i], closest_num)

        return closest_num
