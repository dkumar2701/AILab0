def order(data, stats):
	size = len(data)
	newdata = []
	for j in range(size):
		smallest = data[0]
		for i in range(len(data)):
			if data[i] < smallest:
				smallest = data[i]
		newdata.append(smallest)
		data.remove(smallest)
	for value in newdata:
		data.append(value)

	mean = (sum(newdata)/size)//1

	if size%2 == 0:
		median = newdata[int(size/2)-1]
	else:
		median = newdata[int((size-1)/2)]
	
	modeDict = {newlist: 0 for newlist in newdata}
	for i in range(size):
		modeDict[newdata[i]] += 1

	largest = newdata[0]
	for k, v in modeDict.items():
		if v > modeDict[largest]:
			largest = k
	mode = largest
	stats[0] = mean
	stats[1] = median
	stats[2] = mode
	
	
	return 0


