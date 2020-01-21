# https://leetcode.com/problems/minimum-cost-to-connect-sticks
# Connect ropes
# Connect sticks

import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        temp = 0
        while len(sticks)>1:
            temp += heapq.heappop(sticks)
            temp += heapq.heappop(sticks)
            heapq.heappush(sticks, temp)
            cost += temp
            temp = 0
        return cost