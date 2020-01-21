import heapq
def meeting_rooms(intervals):
	intervals.sort(key= lambda x: x[0])
	# print(intervals)
	if len(intervals) == 0:
		return 0
	mh = []
	heapq.heapify(mh)
	c = 0
	heapq.heappush(mh, intervals[0][1])
	for i in range(1,len(intervals)):
		
		if mh[0] <= intervals[i][0]:
			heapq.heappop(mh)
		heapq.heappush(mh,intervals[i][1])

	return len(mh)

def meeting_rooms_2(intervals):
	s = list(map(lambda x: x[0], intervals))
	e = list(map(lambda x: x[1], intervals))
	s.sort()
	e.sort()
	i = 0
	j = 0
	c = 0
	while i < len(intervals):
		if s[i] >= e[j]:
			j+=1
			c-=1
		
		i+=1
		c+=1

	return c
	


if __name__ == '__main__':
	ip = [[2,15],[36,45],[9,29],[16,23],[4,9]]
	ip = [[7,10],[2,4]]
	ip = []
	ip = [[9,10],[4,9],[4,17]]
	ip = [[2,5]]
	print(meeting_rooms_2(ip))
