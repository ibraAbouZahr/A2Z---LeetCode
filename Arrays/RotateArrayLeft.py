class Solution(object):
    def rotate(self, nums, k):
        temp = 0
        i = 0

        while(i < k):
            temp = nums.pop()
            nums.insert(0,temp)
            i+=1
          
        return nums

# pop elements from the end
# insert elements at front

solution = Solution()
print(solution.rotate([2,2,1], 2))           