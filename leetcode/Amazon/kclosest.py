# https://leetcode.com/problems/k-closest-points-to-origin
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        mh = []
        for i in range(K):
            dist =(-1) * (pow(points[i][0],2) + pow(points[i][1],2))
            heapq.heappush(mh, (dist, points[i]))
        for i in range(K, len(points)):
            dist =(-1) * (pow(points[i][0],2) + pow(points[i][1],2))
            if mh[0][0] < dist:
                heapq.heappushpop(mh, (dist, points[i]))
        
        return [p[1] for p in mh]