class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        while nums:
            x=min(nums)
            temp.append(x)
            nums.remove(x)
        
        nums.extend(temp)