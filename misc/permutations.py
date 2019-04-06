import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = list()
        cut = 0
        # nums_arr = [a for a in nums]
        lst = self.permute_rec(nums, lst,0)
        return lst
    def permute_rec(self,nums, lst,fixed):
        if fixed == len(nums)-1:

            lst.append(nums)
            # print(lst)
            return lst
        for i in range(fixed,len(nums)):
                temp = copy.deepcopy(nums)
                temp[fixed], temp[i] = temp[i], temp[fixed]
                # print(temp)
                lst = self.permute_rec(temp, lst,fixed+1)

        return lst
if __name__ == '__main__':
    s = Solution()
    nums= [1,2,3]
    print(s.permute(nums))