class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        while True:
            return nums[-k]