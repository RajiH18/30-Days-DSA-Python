class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum=0
        result=[]
        for i in nums:
            sum=sum+i
            result.append(sum)
        return result
        