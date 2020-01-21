import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        counts = collections.defaultdict(int)
        for n in nums:
            counts[n] = counts[n]+1
        coll = [(v,k) for k,v in counts.items()]
        print(coll)
        mh = []
        for i in range(len(coll)):
            heapq.heappush(mh, coll[i])
        coll = heapq.nlargest(k, mh)
        return [op[1] for op in coll]

if __name__ == '__main__':
    s = Solution()
    nums = [4,1,-1,2,-1,2,3]

    k = 2
    print(s.topKFrequent(nums, k))