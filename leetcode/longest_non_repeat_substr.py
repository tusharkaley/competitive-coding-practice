class Solution:
    def lengthOfLongestSubstring(self, s):
        letter_store = dict()
        longest_str = 0
        running_count = 0
        for i, ch in enumerate(s):
            if ch not in letter_store:
                letter_store[ch] = i
                running_count +=1
                if running_count >= longest_str:
                    longest_str = running_count
            else:
                running_count = i - letter_store[ch]

                for key in letter_store.keys():
                    if letter_store[key] < letter_store[ch]:
                        del letter_store[key]
                letter_store[ch] = i
                if running_count >=longest_str:
                    longest_str = running_count
        return longest_str

if __name__ == "__main__":
    s = Solution()
    ip = "dvdf"
    print(s.lengthOfLongestSubstring(ip))