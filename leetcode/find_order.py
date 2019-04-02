class Solution:
	def findOrder(self, numCourses, prerequisites):
		prereqs = dict()
		active_pr = list()
		done = list()

		for pr in prerequisites:
			if pr[0] not in prereqs:
				prereqs[pr[0]] = [pr[1]]
			else:
				prereqs[pr[0]].append(pr[1])
		# print(prereqs)
		seen = list()
		for i in range(numCourses):
			stack = list()
			# print("i: {}".format(i))
			if i not in done:
				# print("inside")
				done.extend(self.build_order(i, stack, prereqs, done, seen))
				if -1 in done:
					return []
					# break
		return done
	def build_order(self, course, stack, prereqs, done, seen):
			# print("course: {}".format(course))
			
			if course in seen:
				stack.append(-1) 
				return stack
			seen.append(course)
			# print(stack)
			if course not in prereqs:
				if course not in stack:
					stack.append(course) 
				return stack
			else:

				for j in prereqs[course]:
					if j not in stack:
						if j not in done:
							# stack.append(j)
							self.build_order(j, stack, prereqs, done, seen)
				stack.append(course)
				return stack

if __name__ == '__main__':
	s = Solution()
	# print(s.canFinish(8,[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))

	print(s.findOrder(3,[[1,0],[2,1],[2,0]]))
	print(s.findOrder(2,[[1,0],[0,1]]))
	print(s.findOrder(3,[[1,0],[2,1],[0,2]]))
	# print(s.canFinish(100,[[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],[18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],[18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],[2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],[50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],[35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],[13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],[24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],[46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23],[52,55],[43,59],[49,26],[25,90],[52,0],[55,8],[7,23],[97,41],[0,40],[69,47],[73,68],[10,6],[47,9],[64,24],[95,93],[79,66],[77,21],[80,69],[85,5],[24,48],[74,31],[80,76],[81,27],[71,94],[47,82],[3,24],[66,61],[52,13],[18,38],[1,35],[32,78],[7,58],[26,58],[64,47],[60,6],[62,5],[5,22],[60,54],[49,40],[11,56],[19,85],[65,58],[88,44],[86,58]]))
	# print(s.canFinish(3,[[1,0],[2,1],[0,2]]))
	print(s.findOrder(7,[[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))





			

