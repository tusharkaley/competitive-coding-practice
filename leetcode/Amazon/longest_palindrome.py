class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(l, r):
            print("{}:{}".format(l,r))
            while l>=0 and r<len(s):

                if s[l] == s[r]:
                    print("if")
                    l-=1
                    r+=1
                else:
                    print("else")
                    break
            print("After {}:{}".format(l,r))

            return r-l-1, l+1 , r
        p_m = 0
        p = ""
        if len(s)== 1:
            return s
        for i in range(len(s)):
            temp_l, st, e = check_palindrome(i,i)
            if temp_l > p_m:
                p_m = temp_l
                p =  s[st:e]      
        for i in range(1,len(s)):
            temp_l, st, e  = check_palindrome(i-1,i)
            print(temp_l)
            if temp_l > p_m:
                p_m = temp_l
                p =  s[st:e] 
        return p

if __name__ == '__main__':
    s = Solution()
    ip = "aa"
    print(s.longestPalindrome(ip))