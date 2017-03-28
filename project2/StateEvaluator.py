import heapq
import math
from Queue import Queue

def evaluate(grid):
	# if not len(grid.getAvailableCells()):
	# 	return math.log(grid.getMaxTile(), 2)
	maxTile = grid.getMaxTile()
	# if maxTile:
	# 	maxTile = math.log(maxTile, 2)

	return emptySpacesHeuristic(grid, math.log(maxTile, 2)) + monotonicityRowCol2(grid, 1)

	# return monotonicityRowCol(grid, 1)

def emptySpacesHeuristic(grid, weight):
	# if len(grid.getAvailableCells()) >= 3:
	# 	return weight * 5
	# else:
	# 	return 0
	
	return weight * len(grid.getAvailableCells())

def monotonicityRowCol2(grid, weight):
	maxTile = grid.getMaxTile()
	result = 0

	if grid.getCellValue((0, 0)) == maxTile:
		result += maxTile

	# isMonotonic = True

	# rows
	for y in range(0, 4):
		# if not isMonotonic:
		# 	break

		minVal = None

		if y % 2:
			# y is odd
			for x in range(3, -1, -1):

				if minVal is None:
					minVal = grid.getCellValue((y, x))

				else:
					value = grid.getCellValue((y, x))

					if value > minVal:
						#isMonotonic = False
						result -= (value)

					elif value < minVal:
						minVal = value
		else:
			# y is even
			for x in range(0, 4):

				if minVal is None:
					minVal = grid.getCellValue((y, x))

				else:
					value = grid.getCellValue((y, x))

					if value > minVal:
						#isMonotonic = False
						result -= (value)

					elif value < minVal:
						minVal = value


	# cols
	for x in range(0, 4):
		minVal = None

		for y in range(0, 4):

			if minVal is None:
				minVal = grid.getCellValue((y, x))

			else:
				value = grid.getCellValue((y, x))

				if value > minVal:
					result -= (value)

				elif value < minVal:
					minVal = value

	return weight * result

# currently 2 pass, could be one pass with hashing row/col values
def monotonicityRowCol(grid, weight):
	result = 0

	if grid.getCellValue((0, 0)) == grid.getMaxTile():
		result += 20

	# rows
	for y in range(0, 4):
		minVal = None

		for x in range(0, 4):

			if minVal is None:
				minVal = grid.getCellValue((y, x))

				if minVal:
					minVal = math.log(minVal, 2)

			else:
				value = grid.getCellValue((y, x))

				if value:
					value = math.log(value, 2)

				if value > minVal:
					result -= ((value - minVal) * 2)

				elif value < minVal:
					minVal = value

	# cols
	for x in range(0, 4):
		minVal = None

		for y in range(0, 4):

			if minVal is None:
				minVal = grid.getCellValue((y, x))

				if minVal:
					minVal = math.log(minVal, 2)

			else:
				value = grid.getCellValue((y, x))

				if value:
					value = math.log(value, 2)

				if value > minVal:
					result -= ((value - minVal) * 2)

				elif value < minVal:
					minVal = value

	return weight * result


def monotonicityBFSHeuristic(grid, weight):
	result = 0

	exploredSet = set()
	fringeSet = set([(0, 0)])

	bfsQueue = Queue()
	bfsQueue.put(((0, 0), 0))

	prevDepthValue = None
	currentDepthValue = float("inf")
	lastDepth = -1

	if grid.getCellValue((0, 0)) == grid.getMaxTile():
		# result += (math.log(grid.getMaxTile(), 2) * 4)
		result += 20

	# if len(grid.getAvailableCells()) < 3:
	# 	return weight * result

	while not bfsQueue.empty():
		(pos, currentDepth) = bfsQueue.get()

		value = grid.getCellValue(pos)

		if value:
			value = math.log(value, 2)
		else:
			value = 0

		if pos in fringeSet:
			fringeSet.remove(pos)

		exploredSet.add(pos)

		if currentDepth == lastDepth + 2:
			lastDepth += 1

			if prevDepthValue is None or prevDepthValue > currentDepthValue:
				prevDepthValue = currentDepthValue
				currentDepthValue = float("inf")

		if currentDepthValue > value:
			currentDepthValue = value

		if currentDepth == lastDepth + 1:
			if prevDepthValue is not None:
				
				if value < prevDepthValue:
					result += 0
				else:
					result -= ((value - prevDepthValue) + value)
		
		children = []

		if pos[0] + 1 <= 3:
			children.append((pos[0] + 1, pos[1]))
		if pos[1] + 1 <= 3:
			children.append((pos[0], pos[1] + 1))

		for child in children:
			if child not in fringeSet and child not in exploredSet:
				fringeSet.add(child)
				bfsQueue.put((child, currentDepth + 1))

	return weight * result

def employSnakeStrategy(grid):
	result = 0
	minHeap = []

	# gather large tiles in a heap
	for y in range(0, 4):
		for x in range(0, 4):

			value = grid.getCellValue((x, y))

			if value:
				heapq.heappush(minHeap, (-value, (x, y)))

	currentVal = None
	prevVal = None

	# 0 1 2 3
	# 7 6 5 4
	# 8 9 10 11
	# 15 14 13 12

	for i in range(0, len(minHeap)):
		y = i / 4
		x = None
		if y % 2 == 0:
			# if y is even
			x = i % 4
		else:
			# if y is odd
			x = 3 - (i % 4)

		currentVal = grid.getCellValue((x, y))
		(heapValue, heapPos) = heapq.heappop(minHeap)
		heapValue = -heapValue

		if currentVal == heapValue:
			result += 3

			if x == 0 and y == 0:
				result += 10


	return result

def edgeHeuristic(grid):
	minHeap = []
	result = 0

	for y in range(0, 4):
		for x in range(0, 4):

			value = grid.getCellValue((x, y))

			if value and value > 16:
				if len(minHeap) >= 4:
					(topValue, _) = minHeap[0]
					if value > topValue:
						heapq.heappop(minHeap)
						heapq.heappush(minHeap, (value, (x, y)))
				else:
					heapq.heappush(minHeap, (value, (x, y)))

	for i in range(len(minHeap), 0, -1):
		(value, pos) = heapq.heappop(minHeap)

		# check if the max value is in the corner
		if i == 1:
			if pos[0] == 0 and pos[1] == 0:
				result += 10
			elif pos[0] == 0 and pos[1] == 4:
				result += 10
			elif pos[0] == 4 and pos[1] == 0:
				result += 10
			elif pos[0] == 4 and pos[1] == 4:
				result += 10

		if pos[0] == 0 or pos[0] == 4 or pos[1] == 0 or pos[1] == 4:
			result += 1

	return result
