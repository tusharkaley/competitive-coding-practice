# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/submissions/
class Solution:
    def minDominoRotations(self, A, B):
        def check(x):
            ra = rb =0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    ra+=1
                elif B[i] != x:
                    rb+=1
            return min(ra,rb)
        
        rot = check(A[0])
        # print(rot)
        if rot != -1 or A[0]==B[0]:
            return rot
        else:
            return check(B[0])

if __name__ == '__main__':
    s = Solution()
    # a = [3,5,1,2,3]
    # b = [3,6,3,3,4]
    a =  [2,1,2,4,2,2] 
    b = [5,2,6,2,3,2]
    print(s.minDominoRotations(a,b))