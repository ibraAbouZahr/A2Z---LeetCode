class Solution(object):
    def moveZeroes(self, nums):
       index = 0
       temp = 0
       for i in range (len(nums)):
           if nums[i] != 0:
               temp = nums[i]
               nums[i] = nums[index]
               nums[index] = temp
               index+=1       
       return nums
   
   
# Another way to swap in python: nums[i], nums[index] = nums[index], nums[i]  
 
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))