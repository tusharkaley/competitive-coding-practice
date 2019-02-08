def solution(words):
	op = list()
	for word in words:
		op.append(change_count(word))
	return op
def change_count(word):
	pos = 0
	count = 0
	win = 0
	i = 0
	while i <= len(word)-2:
		live = i
		j_mat = False
		for j in (1,3):
			if live+j < len(word):
				if word[live]!=word[j+live]:
					if j==1:
						i = i+1
						break
					if j == 2:
						break

				if word[live]==word[j+live]:
					if j==1:
						i = i+2
						j_mat = True
						count = count + 1
					if j==2:
						if j_mat:
							i = i+1
							break
				
	return count

if __name__ == '__main__':
	wordsl = ["add", "booook", "break"]
	print(solution(wordsl))