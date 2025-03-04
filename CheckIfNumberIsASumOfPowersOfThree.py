class Solution(object):
    def checkPowersOfThree(self, n):  
   
        cap=16
        arr=[]
        for i in range(0,cap):
            arr.append(3**i)
        
        for i in range(cap-1, -1, -1):
            if n>=arr[i]:
                n-=arr[i]
            if n==0:
                return True
        return False
