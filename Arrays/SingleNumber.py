class Solution(object):
    def singleNumber(self, nums):
        
        result = 0
        for i in range (len(nums)):
            result ^= nums[i]
        return result
            
 # XOR operator: ^=            
        
solution = Solution()
print(solution.singleNumber([2,2,1]))           