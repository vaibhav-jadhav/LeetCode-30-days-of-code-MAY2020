class Solution(object):
    def singleNonDuplicate(self, nums):
        t=0
        flag=False
        for x in nums:
            flag=not flag
            if flag :
                print("ok")
                t=t+x
            else:
                print("not ok")
                t=t-x
        return t
