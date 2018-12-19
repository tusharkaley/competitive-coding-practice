import math


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        len_shortest_str = len(strs[0])
        count = 0
        lcp = ""
        exit_now = False
        for stng in strs:
            if len(stng) < len_shortest_str:
                len_shortest_str = len(stng)
        for i in range(0, len_shortest_str):
            char_check = strs[0][i]
            for stng in strs:
                if stng[i] == char_check:
                    continue
                else:
                    exit_now = True
                    break
            if not exit_now:
                lcp = lcp + char_check
        return lcp

if __name__ == "__main__":
    sol = Solution()
    ip = ["dog"]
    print(sol.longestCommonPrefix(ip))