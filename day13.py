class Solution(object):
    def removeKdigits(self, num, k):
        while(k):
            if(k >= len(num)):
                return "0"
            k-=1
            i = 0
            while(i<len(num)-1):
                if(num[i]>num[i+1]):
                    break
                i+=1
            num = num[:i] + num[i+1:]
            
        return str(int(num))
