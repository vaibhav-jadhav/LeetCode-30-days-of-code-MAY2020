def isBadVersion(v):
  vs=[False,True,False,False,True]
  #  vs=[True,False,True,True,True]
  return(vs[v-1])
def firstBadVersion(n):
    l=0
    if isBadVersion(1):
        return 1
    elif isBadVersion(n) == False:
        return 0
    elif isBadVersion(1) == False and isBadVersion(2) == True:
        return 2     
    else:    
        l=2
        r=n
        while l <= r: 
            mid = l + (r - l) // 2;
            if isBadVersion(mid)== True and isBadVersion(mid-1) == False:
                return mid
            if isBadVersion(mid)== True and isBadVersion(mid-1) == True:
                r=mid-1
            if isBadVersion(mid)== False and isBadVersion(mid-1) == False: 
                l=mid+1       

print(firstBadVersion(5))