class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table=dict()
        for x in range(len(nums)):
            if nums[x] in hash_table:
                return [hash_table[nums[x]],x]
            else:
                hash_table[target - nums[x]] = x