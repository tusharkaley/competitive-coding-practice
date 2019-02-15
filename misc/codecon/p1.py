import sys

data = ["www", "banana", "nab", "ban", "band", "bandana"]
# data = ["ww", "soften","listen","quite","ballot","route","muddle","sentinel"]
mesa_dict = dict()
count = 0
i=0
for line in data :
	if i ==0:
		i=i+1
		continue
	else:
		temp_dict = dict()
		temp = "".join(set(line))
		u_str = "".join(sorted(temp))
		

		if u_str not in mesa_dict:
			mesa_dict[u_str] = 1
		else:
			mesa_dict[u_str] = mesa_dict[u_str]+1
for key, value in mesa_dict.items():
	if value != 1:
		count =count + value
print(count)