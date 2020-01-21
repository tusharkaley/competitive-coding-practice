class Solution:
    def twoSum(self, nums, target):
        store = dict()
        ind = 0
        for i in nums:
            
            if i in store:
                store[i].append(ind)
            else:
                store[i] = [ind]
            ind+=1
        print(store)  
        for i in nums:
            temp = target - i

            if temp == i and len(store[i])>1:
                return store[i]
            if temp in store and temp!=i:
                return store[temp]+ store[i]

if __name__ == '__main__':
    s = Solution()
    nums = [3,3]
    target = 6
    # nums =[3,2,4]

    # target = 6
    print(s.twoSum(nums, target))
