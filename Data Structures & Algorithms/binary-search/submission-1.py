class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag='red'
        for i in nums:
            if i==target:
                flag='green'
                return nums.index(target)
                break
        if flag=='red':
            return -1