def maximumToys(prices, k):
	prices.sort()
	count = 0
	for p in prices:
		k = k-p
		if k>0:
			count = count + 1
		else:
			break
	return count
	
if __name__ == '__main__':
	ip = [1,12,5,111,200,1000,10]
	bud = 50
	maximumToys(ip, bud)