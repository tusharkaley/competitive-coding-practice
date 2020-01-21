# Amazon | OA 2019 | Optimal Utilization
def optimal_utilization(a, b, t):
	
	if len(a) ==0 or len(b) == 0:
		return []
	
	a.sort(key = lambda x: x[1])
	b.sort(key = lambda x: x[1])

	if (a[0][1] + b[0][1]) > target:
		return []
	def helper(i, j, t):
		if a[i][1] + b[j][1]> target:
			return
		if a[op[0][0]][1] + b[op[0][1]][1] ==  
	op = [[0, 0]]
	
	
# Someone's solution

def amazon(a, b, target):
  a.sort(key=lambda x: x[1])
  diff = float('inf')
  output = []
  for i in range(len(b)):
    index = bsearch(a, target - b[i][1])
    if target - a[index][1] - b[i][1] == diff:
      output.append([a[index][0], b[i][0]])
      index -= 1
      while index >= 0 and target - a[index][1] - b[i][1] == diff:
        output.append([a[index][0], b[i][0]])
        index -= 1
    elif 0 <= target - a[index][1] - b[i][1] < diff:
      diff = target - a[index][1] - b[i][1]
      output = [[a[index][0], b[i][0]]]
      index -= 1
      while index >= 0 and target - a[index][1] - b[i][1] == diff:
        output.append([a[index][0], b[i][0]])
        index -= 1
  return output if output else [[]]
def bsearch(arr, target):
  left = 0
  right = len(arr) - 1
  while left < right:
    mid = (left + right) // 2 + 1
    if arr[mid][1] == target:
      return mid
    elif arr[mid][1] < target:
      left = mid
    else:
      right = mid - 1
  return right
