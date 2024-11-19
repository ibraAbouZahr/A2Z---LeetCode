class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range (len(x)//2):
            j = len(x) - 1 - i
            if(x[i]!=x[j]):
                return False
        return True

solution = Solution()
print(solution.isPalindrome(121)) 

        