from typing import List

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        RANGE_ARRAY = [lo]
        lowestNumber = lo
       
       
        while(lowestNumber < hi):
            lowestNumber += 1
            RANGE_ARRAY.append(lowestNumber)
            

        OPERATIONS_ARRAY = []

        for i in range(len(RANGE_ARRAY)):
            num = RANGE_ARRAY[i] 
            operations = 0  
            while num != 1:
                if num % 2 == 0:
                    num /= 2
                else:
                    num = num * 3 + 1
                operations += 1
            OPERATIONS_ARRAY.append(operations)


        final_number = 0

        POWER_MAP = {}
        for keys, values in zip(RANGE_ARRAY, OPERATIONS_ARRAY):
            POWER_MAP[keys] = values

        COPY_OF_OPERATIONS_ARRAY = sorted(OPERATIONS_ARRAY)


        for keys, values in POWER_MAP.items():
            if COPY_OF_OPERATIONS_ARRAY[k-1] == values:
                final_number = keys
        

        return final_number
    
class Solution:
    def makeFancyString(self, s: str) -> str:
        WORD_STACK = []
        count = 0

        for i in range(len(s)):
            WORD_STACK.append(s[i])
            if i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
            else:
                count = 0
            
            if count == 2:
                WORD_STACK.pop()
                count -= 1

        return ''.join(WORD_STACK)
    
# 1752. Check if Array Is Sorted and Rotated
    

# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

class Solution:
    def check(self, nums: List[int]) -> bool:

        count_drop = 0

        for i in range(len(nums)):
            current = nums[i]
            next = nums[(i + 1) % len(nums)]

            if(current > next):
                count_drop += 1
                if count_drop > 1:
                    return False
        
        return count_drop <= 1

solution = Solution()
nums = [3,4,5,1,2] 
nums1 = [2,1,3,4]
nums2 = [1,2,3]
nums3 = [3,4,4,5,1,2]
nums4 = [3,2,1,4,5]
nums5 = [11,11,1,20]
result = solution.check(nums)
result1 = solution.check(nums1)
result2 = solution.check(nums2)
result3 = solution.check(nums3)
result4 = solution.check(nums4)
result5 = solution.check(nums5)
print(result)  
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

