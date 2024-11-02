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

