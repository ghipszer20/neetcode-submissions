class Solution:

    # Optimal: HashSet: O(n) time, O(n) space
    def hasDuplicate(self, nums):
        hshSet = set()

        for num in nums:
            if num in hshSet:
                return True

            hshSet.add(num)
            
        return False

    # Base Case: O(n^2) time, O(1) space
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
        
    #     return False


        