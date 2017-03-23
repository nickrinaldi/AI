import heapq

def evaluate(grid):
	return emptySpacesHeuristic(grid) + edgeHeuristic(grid)


def emptySpacesHeuristic(grid):
	return len(grid.getAvailableCells())

def edgeHeuristic(grid):
	minHeap = []
	result = 0

	for y in range(0, 4):
		for x in range(0, 4):

			value = grid.getCellValue((x, y))

			if value:
				if len(minHeap) < 4:
					heapq.heappush(minHeap, (value, (x, y)))
				elif value > minHeap[0][0]:
					heapq.heappop(minHeap)
					heapq.heappush(minHeap, (value, (x, y)))

	for i in range(0, len(minHeap)):
		(value, pos) = heapq.heappop(minHeap)

		# check if the max value is in the corner
		if i == 4:
			if pos[0] == 0 and pos[1] == 0:
				result += 1
			elif pos[0] == 0 and pos[1] == 4:
				result += 1
			elif pos[0] == 4 and pos[1] == 0:
				result += 1
			elif pos[0] == 4 and pos[1] == 4:
				result += 1

		if pos[0] == 0 or pos[0] == 4 or pos[1] == 0 or pos[1] == 4:
			result += 1

	result += (4 - i)
	return result
