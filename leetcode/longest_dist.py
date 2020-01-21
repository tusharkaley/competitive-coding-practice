

class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		self.cities_store = dict()
		
		
	def longest_distance(self, cities_dist):
		[start, end, dist] = cities_dist.split(":")
		dist = int(dist)
		d_start = 0
		op_start = list()
		op_end = list()	
		d_end = 0
		ret_val = None

		if len(self.cities_store) == 0:
			self.cities_store[start] = (dist, end)
			self.cities_store[end] = (dist, start)

			return None
		else:
			if start in self.cities_store:
				d_start = self.cities_store[start][0]+ dist
				op_start = [self.cities_store[start][1], start, end]
				op_start.sort()

				

				if dist > self.cities_store[start][0]:
					self.cities_store[start] = (dist, end)
			else:
				self.cities_store[start] = (dist, end)
			
			if end in self.cities_store:
				d_end = self.cities_store[end][0]+ dist
				op_end = [self.cities_store[end][1], start, end]
				op_end.sort()

				if dist > self.cities_store[end]:
					self.cities_store[end] = (dist, start)
			else:
				self.cities_store[end] = (dist, start)
			
			if op_start and op_end:
				# check dists
				if d_start > d_end:
					ret_val = "{}:{}:{}:{}".format(d_start, op_start[0], op_start[1], op_start[2])
				else:
					ret_val = "{}:{}:{}:{}".format(d_end, op_end[0], op_end[1], op_end[2])
			elif op_start and not op_end:
				ret_val = "{}:{}:{}:{}".format(d_start, op_start[0], op_start[1], op_start[2])
			elif op_end and not op_start:
				ret_val = "{}:{}:{}:{}".format(d_end, op_end[0], op_end[1], op_end[2])
			
			return ret_val

if __name__ == '__main__':
	s = Solution()
	print(s.longest_distance("CHI:www:10"))
	print(s.longest_distance("rrr:LA:40"))
	print(s.longest_distance("ttt:ggg:60"))
	print(s.longest_distance("NYC:HAWAII:100"))

