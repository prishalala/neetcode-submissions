class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=[]
        while len(arr)>1:
            arr.remove(arr[0])
            l.append(max(arr))
            
        l.append(-1)
        return l