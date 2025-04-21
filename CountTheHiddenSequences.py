class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        min_val, max_val = 0, 0
        _sum = 0
        for x in differences:
            _sum+=x
            min_val = min(min_val, _sum)
            max_val = max(max_val, _sum)
        min_val = lower-min_val
        max_val = upper-max_val
        return 0 if min_val>max_val else max_val-min_val+1
        
