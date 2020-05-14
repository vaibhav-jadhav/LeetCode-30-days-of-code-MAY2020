def majorityElement(nums):
    record=dict()
    for element in nums:
        if element not in record:
            record[element]=1
        else:
            record[element]=record[element]+1
    for key in record:
       if record[key] > len(nums)/2:
           return key
print(majorityElement([3,2,3]))
        
        
    