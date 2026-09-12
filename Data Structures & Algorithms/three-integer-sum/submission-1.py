class Solution:

    ## Sorting initial solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_size = len(nums)
        nums.sort()
        ans = []

        for i in range(nums_size):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = nums_size - 1
            target = 0 - nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif nums[j] + nums[k] > target:
                    k -= 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                
                else:
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return ans

            





    ## Brute Force: O(n^3) time, O(n^3) space
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     ans = set()

    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             for k in range(j + 1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     temp_set = set(nums[i], nums[j], nums[k])

    #                     if temp_set not in ans:
    #                         ans.add(temp_set)

    #     ans_list = []

    #     for sub_set in ans:
    #         temp_list = []
    #         for num in sub_set:
    #             temp_list.append(num)
    #         ans_list.append(temp_list)

    #     return ans_list


        