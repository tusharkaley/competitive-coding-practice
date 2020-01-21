class Solution:
    def validUtf8(self, data):
        n_b = 0
        mask1 = 1<<7
        mask2 = 1<<6
        for num in data:
            
            if n_b==0:
                mask = 1<<7
                while mask & num:
                    n_b+=1
                    mask = mask >> 1
                if n_b ==0:
                    continue
                if n_b ==1 or n_b>4:
                    return False
            else:
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_b-=1
        return n_b ==0

if __name__ == '__main__':
	s = Solution()
	ip = [197, 130, 1]
	print(s.validUtf8(ip))