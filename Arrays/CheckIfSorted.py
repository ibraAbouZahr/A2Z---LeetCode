class Solution(object):
    def check(self, nums):
        Flag = False
        for i in range (len(nums)-1):
            if nums[i] < nums[i+1]:
                Flag = True
            elif nums[i] > nums[i+1]:
                Flag = False
                print("false")
                return
        if Flag != False:
            print("true") 
      
solution = Solution()
print(solution.check([1,1,2]))