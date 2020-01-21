 # Critical Connections in a Network 
 # Bridges
import collections
class Nodes:
	def __init__(self, st, ln, p, vi):
		self.st = st
		self.ln = ln
		self.p = p
		self.vi = vi

def critical_connections(n, connections):
	
	def dfs(nodes, cur, bridges, st, source):
		
		nodes[cur].p = source
		nodes[cur].st = st
		nodes[cur].ln = st
		nodes[cur].vi = True
		
		nei = adj_list[cur]
		print(nei)
		for n in nei:
			if nodes[n].vi== False:
				dfs(nodes, n, bridges, st+1, cur)
		print("outside")
		# print(cur)
		# print([nodes[n].ln if nodes[cur].p != n else float("inf") for n in adj_list[cur]])
		# print([nodes[n].ln for n in adj_list[cur]])
		nodes[cur].ln = min([nodes[n].ln if nodes[cur].p != n else float("inf") for n in adj_list[cur]])
		# nodes[cur].ln = min([nodes[n].ln for n in adj_list[cur]])
		print(nodes[cur].ln)
		
		if nodes[nodes[cur].p].ln < nodes[cur].ln:
				bridges.append([source, cur])
				print(bridges)
			

	adj_list = [[] for i in range(n)]
	nodes = [0]*n
	for c in connections:
		adj_list[c[0]].append(c[1])
		adj_list[c[1]].append(c[0])
	print(adj_list)
	for i in range(n):
		nodes[i] = Nodes(-1,-1,-1,False)
	bridges = []
	dfs(nodes, 0, bridges, 0, 0)
	return bridges

if __name__ == '__main__':
	n = 6
	con = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]
	print(critical_connections(n, con))