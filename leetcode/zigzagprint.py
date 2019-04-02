class Solution:
    def convert(self, s, numRows):
        index_dict = list()
        rows_dict = dict()
        index = 1
        add = True
        if numRows == 1:
        	return s
        for i in range(1, numRows+1):
        	rows_dict[i] = ""
        for ch in s:
        	index_dict.append(index)
        	rows_dict[index] = rows_dict[index]+ch
        	if add:
        		index = index + 1
        	else:
        		index = index - 1
        	if index == numRows:
        		add = False
        	if index == 1:
        		add = True
        op = ""
        for values in rows_dict.values():
        	op = op + values
        return op


if __name__ == '__main__':
	s = Solution()
	print(s.convert("PAYPALISHIRING", 4))

