# Leetcode Problem

# 227. Basic Calculator II

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


class Solution:
    def calculate(self, s: str) -> int:
        num=0;stack =[]; sign = "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
                
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
                
        return sum(stack)