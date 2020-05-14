class Solution:
    def findComplement(self, num: int) -> int:
        b=str("{0:b}".format(num))
        print(b)
        str1=""
        for l in b:
            if l is "0":
                str1=str1+"1"
            if l is "1":
                str1=str1+"0"
        return (int(str1,2))
