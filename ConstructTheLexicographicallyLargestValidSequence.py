class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (2 * n - 1)  
        used = [False] * (n + 1)    

        def backtrack(index):
            if index == len(result):
                return True  

            if result[index] != 0:
                return backtrack(index + 1)  

            for num in range(n, 0, -1):
                if not used[num]:
                    if num == 1:
                        result[index] = num
                        used[num] = True
                    else:
                        next_index = index + num 
                        if next_index < len(result) and result[next_index] == 0:
                
                            result[index] = num
                            result[next_index] = num
                            used[num] = True
                        else:
                            continue  
                   
                    if backtrack(index + 1):
                        return True  

                    result[index] = 0
                    if num == 1:
                        used[num] = False
                    else:
                        result[next_index] = 0
                        used[num] = False

            return False 

        backtrack(0) 
        return result
