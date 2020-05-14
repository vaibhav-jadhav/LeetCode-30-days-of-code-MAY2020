def firstUniqChar(s1): 
    record=dict()
    s=s1[0:]
    for ind,value in enumerate(s):
            if value not in record:
                record[value]=1
            else:
                record[value]=record[value]+1
            if value in record:
                re
    flag=False
    for key in record:
        if record[key]==1:
            flag=True
            return(s.index(key))
    if not flag:
        return(-1)  
    print(record)
    
print(firstUniqChar("leetcode"))
    
