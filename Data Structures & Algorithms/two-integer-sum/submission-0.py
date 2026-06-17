class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,j in enumerate(nums):
            complement=target-j
            if complement in map:
                return [map[complement], i]
            map[j]=i
        return

