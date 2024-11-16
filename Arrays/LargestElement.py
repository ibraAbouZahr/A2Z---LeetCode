from typing import List

class Solution:
    def largest(self, arr : List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        
        else: 
            largest = arr[0];
            for i in range (len(arr)):
                if arr[i] > largest:
                    largest = arr[i]
                
            
        
        return largest
    
        
solution = Solution()
print(solution.largest([-1, 0, 3, -7, 5])) 