class Solution(object):
    def check(self, nums):
        count = 0
        for i in range (len(nums)-1):
            if nums[i] > nums[i+1]:
                count+=1
        if count > 1:
            return False
        if count == 1 and nums[-1] > nums [0]:
            return False
        return True
    
solution = Solution()
print(solution.check([3,4,5,1,2]))