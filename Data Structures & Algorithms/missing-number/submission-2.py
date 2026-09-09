class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        test = []

        for i in range(len(nums) + 1):
            test.append(i)

        return sum(test) - sum(nums)


    # def missingNumber(self, nums: List[int]) -> int:
    #     for i in range(len(nums) + 1):
    #         if i not in nums:
    #             return i
        
    #     return -1
        
        