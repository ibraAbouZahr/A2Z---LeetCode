class Solution(object):
    def missingNumber(self, nums):
        sum = 0
        
        for i  in range (len(nums)):
            sum = sum + nums[i] 
      
        expectedSum = len(nums) * (len(nums) + 1)//2
    
        return expectedSum - sum 
    
solution = Solution()
print(solution.missingNumber([3,0,1]))

# The floor division is //, it removes the decimal part afteer div.