# 402. Remove K Digits

# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while stack and stack[-1] > digit and k:
                stack.pop()
                k-=1
            stack.append(digit)
            
        #edge cases
        
        while k>0:
            stack.pop()
            k-=1
            
        ans = "".join(stack).lstrip("0")
        if ans!="":
            return ans
        else:
            return "0"
