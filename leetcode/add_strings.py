class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        zero_pad = 0
        sum = ""
        if len(num1) > len(num2):
            zero_pad = len(num1)-len(num2)
            num2 = "0"*zero_pad + num2
        if len(num2) > len(num1):
            zero_pad = len(num2) - len(num1)
            num1 = "0" * zero_pad + num1
        carry = 0

        for i in range(len(num1)-1, -1, -1):
            temp_sum = int(num2[i])+int(num1[i])+carry

            if temp_sum>9:
                sum = str(temp_sum%10) + sum
                carry = int(temp_sum/10)
            else:
                sum = str(temp_sum) + sum
                carry = 0
        if carry!=0:
            sum = str(int(carry)) + sum
        return sum

if __name__ == "__main__":
    s =  Solution()
    print(s.addStrings("9", "99"))