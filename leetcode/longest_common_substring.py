def longest_common_substring(str1, str2):
        m = len(str1)
        n = len(str2)
        grid = [[0] * n for i in range(m)]
        longest = 0
        longest_i = 0
        for i in range(m):
            for j in range(n):
                # print("Comparing {} and {}".format(str1[i],str2[j]))
                if str1[i] == str2[j]:
                    if i!=0 and j != 0:
                        if grid[i-1][j-1]==0:
                            grid[i][j] = 1
                        else:
                            grid[i][j] = grid[i-1][j-1] + 1
                    else:
                        grid[i][j] = 1
                else:
                    grid[i][j]= 0
                if grid[i][j] > longest:
                    longest = grid[i][j]
                    longest_i = i
        # for i in range(m):
        #     for j in range(n):
        #         print grid[i][j],
            # print("")
        print(longest)
        print(longest_i)
        if longest_i-longest <0:
            print (str1[longest_i::-1][::-1])
        else:
            print (str1[longest_i:(longest_i - longest):-1][::-1])
if __name__ == "__main__":
    str1 = "cbbd"
    str2 = str1[::-1]
    longest_common_substring(str1, str2)

    