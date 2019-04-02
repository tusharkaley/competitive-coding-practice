class Solution:
    def minAddToMakeValid(self, S):
        counter = 0
        tmp_counter = 0
        brk = False
        stack = list()
        for s in S:
            if s == "(":
                # push to stack increment counter         
                stack.append("(")
            if s == ")":
                # pop from stack decrement counter
                if stack:
                    stack.pop(0)
                else:
                    counter = counter + 1
        counter = counter + len(stack)
        return(counter)
            

if __name__ == '__main__':
    s = Solution()
    inp = "(()())(("
    print(s.minAddToMakeValid(inp))