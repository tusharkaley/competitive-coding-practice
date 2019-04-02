class Solution:
    def repeatedStringMatch(self, A, B):
        if B in A:
            return 1
        len_a = len(A)
        repeats = 0
        index = 0
        b = B[0]
        pos = A.find(b)
        index = pos
        if index != 0:
            repeats = repeats + 1
        for b in B[:]:
            if b != A[index%len_a]:
                return -1
            else:
                if index%len_a == 0:
                    repeats = repeats + 1
            
            index = index + 1
        return repeats


if __name__ == '__main__':
    s = Solution()
    A = "aaac"
    B = "aac"
    print(s.repeatedStringMatch(A,B))