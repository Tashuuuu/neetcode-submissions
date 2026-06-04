class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = {} # value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in new:
                return [new[diff], i]
            new[n] = i
        return