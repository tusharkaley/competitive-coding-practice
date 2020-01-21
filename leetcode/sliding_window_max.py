class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_pal(m,n):
            l = m
            r = n
            
            while l >= 0 and r<len(s):
                if s[l]==s[r]:
                	l-=1
                	r+=1    
                else:
                    break
                
            l+=1
            r-=1
            return r-l+1
            
        longest = 0
        for i in range(len(s)):
            pal_len = check_pal(i,i)
            if longest < pal_len:
                longest = pal_len
                
        i = 0
        j = 1
        while j < len(s):
            pal_len = check_pal(i,j)
            if longest < pal_len:
                longest = pal_len
            i+=1
            j+=1
        return longest
        
        
if __name__ == '__main__':
	s = Solution()
	print(s.longestPalindrome("babad"))