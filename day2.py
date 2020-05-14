class Solution(object):
    def numJewelsInStones(self, J, S):
        count =0
        for op in J :
            opc=S.count(op)
            count = count + opc
        return count
