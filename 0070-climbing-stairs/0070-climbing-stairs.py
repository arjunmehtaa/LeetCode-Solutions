class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        one, two = 1, 1
        for i in range(n - 1):
            temp = two
            two = one + two
            one = temp
        return two
            
            