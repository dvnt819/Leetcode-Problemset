class Solution(object):
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        res_list = [char for char in dominoes]
        update = True

        while update:
            update = False
            temp = [0] * n

            for i in range(n):
                if res_list[i] == 'L' and i - 1 >= 0:
                    temp[i-1] -= 1
                if res_list[i] == 'R' and i + 1 <= n - 1:
                    temp[i+1] += 1

            for i in range(n):
                if res_list[i] == '.':
                    if temp[i] == -1:
                        res_list[i] = 'L'
                        update = True
                    if temp[i] == 1:
                        res_list[i] = 'R'
                        update = True
        
        return "".join(res_list)     
