# https://leetcode.com/problems/find-duplicate-file-in-system/
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths):
        files = defaultdict(list)
        for path in paths:
            temp = path.split(" ")
            for i in range(1, len(temp)):
                cont = temp[i].split("(")
                if cont[1] in files:
                    files[cont[1]].append(temp[0]+"/"+cont[0])
                else:
                	files[cont[1]].append(temp[0]+"/"+cont[0])
        return ([i for i in files.values() if len(i)>1])

if __name__ == '__main__':
	ip = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
	ip = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
	s = Solution()
	s.findDuplicate(ip)

