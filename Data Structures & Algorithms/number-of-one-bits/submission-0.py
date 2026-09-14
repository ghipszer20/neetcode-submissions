class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0

        while n:
            if n % 2 == 1:
                num_ones += 1
            
            n //= 2

        return num_ones
        