class Solution(object):
    def countLargestGroup(self, n):
        largest, c = 0, 0
        count = {}
        for num in range(1, n + 1):
            s = num // 10**4 + (num // 10**3) % 10 + (num // 10**2) % 10 + (num // 10) % 10 + num % 10
 
            count[s] = count.get(s, 0) + 1
            if largest < count[s]:
                largest = count[s]
                c = 1
            elif largest == count[s]:
                c += 1

        return c
