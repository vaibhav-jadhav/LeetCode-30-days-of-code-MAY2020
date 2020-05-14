class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root=math.sqrt(num)
        if int(root + 0.5) ** 2 == num:
           print(num, "is a perfect square")
           return True
        else:
           print(num, "is not a perfect square")
           return False
