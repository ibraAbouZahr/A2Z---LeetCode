class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        FinalCount = 0
        for i in range (len(nums)):
            if nums[i] == 1:
                count += 1 
                if count > FinalCount:
                    FinalCount = count
            elif nums[i] == 0:
                count = 0
        return FinalCount
        
solution = Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
        