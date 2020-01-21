class Node(object):
	"""docstring for Node"""
	def __init__(self, st, ln, p, vi):
		self.st = st
		self.ln = ln
		self.p = p
		self.vi = vi
def critical_connections(n, connections):
	def dfs(st, source):
		
	nodes = [0]*n
	adj_list = [[] for i in range(n)]
	for conn in connections:
		adj_list[conn[1]].append(conn[0])
		adj_list[conn[0]].append(conn[1])
	for i in range(n):
		nodes[i] = Node(-1,-1,-1,False)


		