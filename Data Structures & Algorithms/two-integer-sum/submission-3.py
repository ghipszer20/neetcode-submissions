class Solution:

    # splicing:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            r_splice = nums[i+1:]
            temp = target - nums[i]
            if temp in r_splice:
                return [i, 1 + i  + r_splice.index(temp)]
                
        return [-1, -1]

    # hashmap: O(n) time, O(n) memory
    # def twoSum(self, nums, target):
    #     hshMap = {}

    #     for i in range(len(nums)):
    #         if target - nums[i] in hshMap:
    #             return [hshMap[target - nums[i]], i]
    #         hshMap[nums[i]] = i
        
    #     return [-1, -1]

    # brute force: O(n^2) time, O(1) memory
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
        
    #     return [-1, -1]

        

                

        
        