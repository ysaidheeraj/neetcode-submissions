class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_table = set([target - nums[i] for i in range(len(nums))])

        for i in range(len(nums)):
            if target - nums[i] in diff_table:
                for j in range(i+1, len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i, j]
