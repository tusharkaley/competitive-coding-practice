import math
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [-1]*(amount+1)
        table[0] = 0
        for i in range(1,amount+1):
            # print(i)
            tmp_list = list()
            for j in coins:
                if i-j >= 0:
                    tmp_list.append(table[i-j])
                # print(tmp_list)
            if tmp_list:
                table[i] = 1+ min(tmp_list)
            else:
                table[i] = float("inf")
        if math.isinf(table[-1]):
            table[-1] = -1
        return table[-1]


if __name__ == '__main__':
    s = Solution()
    coins = [2]
    amount = 4
    # coins = [2]
    # amount = 3
    print(s.coinChange(coins, amount))
