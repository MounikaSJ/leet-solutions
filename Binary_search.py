class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0
        R = N-1

        while L <= R:
            mid = L+(R-L)//2

            if nums[mid] == target:
                return mid
            elif target <= nums[mid]:
                R = mid-1
            else :
                L = mid+1
        
        return -1