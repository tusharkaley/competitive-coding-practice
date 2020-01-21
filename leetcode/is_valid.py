from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = deque()
        open_bracs= ['[','{','(']
        close_bracs = [']', '}',')']

        for ch in s:
        	if ch in open_bracs:
        		brackets.appendleft(ch)
        	if ch in close_bracs:
        		try:
        			temp = brackets.popleft()
        			if ch == ']':
        				if temp != '[':
        					return False
        			if ch == '}':
        				if temp != '{':
        					return False
        			if ch == ')':
        				if temp != '(':
        					return False
        		except Exception as e:
        			return False
        			
        if len(brackets) == 0:
        	return True
        else:
        	return False
if __name__ == '__main__':
	s = Solution()
	st = "()"
	st = "()[]{}"
	st = "(]"
	st = "([)]"
	st = "{[]}"
	st = ']'
	print(s.isValid(st))
        		