class Solution(object):
    def plusOne(self, digits):

        num = 0
        for d in digits:
            num = num * 10 + d 
        num += 1
        
        return [int(d) for d in str(num)] 
