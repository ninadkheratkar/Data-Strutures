# 946. Validate Stack Sequences

# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        N = len(popped)
        i = 0
        for p in pushed:
            stack.append(p)
            while stack and i<N and stack[-1]==popped[i]:
                print(stack[-1])
                print(popped[i])
                i+=1
                stack.pop()
                
        return stack == []
