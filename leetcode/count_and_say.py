class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count_and_say = list()
        first_term = "1"
        count_and_say.append(0)
        count_and_say.append(first_term)
        if n == 1:
            return first_term

        for i in range(2, n + 1):

            temp = ""
            count_elem = 0
            elem = count_and_say[i-1]
            prev_num = elem[0]
            same_elem = ""
            for j in range(0, len(elem)):

                if elem[j] == prev_num:
                    count_elem = count_elem + 1
                    same_elem = str(count_elem) + elem[j]
                else:
                    count_elem = 1
                    if same_elem != "":
                        temp = temp + same_elem
                    if j != len(elem)-1:
                        if same_elem != "" and elem[j+1] != elem[j]:
                            temp = temp + str(count_elem) + elem[j]

                        if same_elem == "" and elem[j+1] != elem[j]:
                            temp = temp + str(count_elem) + elem[j]
                    else:
                        temp = temp + str(count_elem) + elem[j]
                    same_elem = ""

                prev_num = elem[j]

            if same_elem != "":
                temp = temp + same_elem
            new_term = temp
            count_and_say.append(new_term)
            if n == i:
                return new_term

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(6))