class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        p = 1
        for i in range (len(nums)):
            output.append(p)
            p = p * nums[i]

        q = 1    
        for i in range (len(nums)-1, -1, -1):
            output[i]= output[i] * q 
            q = q * nums[i]
        
        return output
        