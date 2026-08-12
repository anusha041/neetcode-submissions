class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        output = 1
        current = 1
        print (nums)
        if len(nums)==0:
            return 0
        i = 1
        while i < (len(nums)):
            if nums[i-1] +1 == nums[i]:
                current+=1
            elif nums[i-1] == nums[i]:
                i+=1
                continue
            else:
                current = 1

            if current>output:
                output = current
            i+=1



        return output

        