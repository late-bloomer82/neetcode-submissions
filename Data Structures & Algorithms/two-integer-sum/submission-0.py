class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            complement_number = target - num
            if complement_number in d:
                return [d[complement_number],i]
            d[num] = i
