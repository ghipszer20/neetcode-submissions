class Solution:

    # Dynamic Programming Approach - two pointers: O(n) time, O(1) space
    def climbStairs(self, n):
        one, two = 1, 1

        for i in range(2, n + 1):
            one, two = one + two, one
        
        return one


    # Dynamic Programming Approach - array: O(n) time, O(n) space
    # def climbStairs(self, n):
    #     arr = [1] * (n + 1)

    #     for i in range(2, len(arr)):
    #         arr[i] = arr[i-1] + arr[i-2]
        
    #     return arr[-1]



    # Recursive Approach: O(2^n) time, O(2^n) space
    # def climbStairs(self, n: int) -> int:
    #     if n == 0 or n == 1:
    #         return 1
        
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        