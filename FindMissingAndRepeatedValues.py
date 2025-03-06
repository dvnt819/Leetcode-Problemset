class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        
        missing = (n * n) * (1 + n * n) // 2 
        seen = set() 
        duplicate = -1
        for row in grid:
            for num in row:
                if num not in seen:
                    seen.add(num)
                    missing -= num 
                else:
                    duplicate = num
                    
        return [duplicate, missing]
