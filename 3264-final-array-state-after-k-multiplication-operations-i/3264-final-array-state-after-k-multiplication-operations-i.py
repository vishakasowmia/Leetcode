class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        count = 1
        while count <= k:
            x = min(nums)
            mul = x*multiplier
            for i in range(len(nums)):
                if nums[i] == x:
                    nums[i] = mul
                    break
            count +=1
        return nums
            