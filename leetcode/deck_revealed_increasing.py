class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort(reverse=True)
        res = []
        for num in deck:
            if len(res) == 0:
                res.append(num)
            else:
                temp = res.pop()
                res.insert(0,temp)
                res.insert(0,num)
        return res

if __name__ == '__main__':
	s = Solution()
	inp = [17,13,11,2,3,5,7]
	print(s.deckRevealedIncreasing(inp))