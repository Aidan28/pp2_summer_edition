class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[]
        ans.append(0)
        for i in range(0,len(gain)):
            tmp=ans[i]+gain[i]
            ans.append(tmp)
            
        return max(ans)