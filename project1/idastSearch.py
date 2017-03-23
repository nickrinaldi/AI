import heapq
from timeit import time
from game_state import GameState
from output import output

def idastSearchFindPath(initialState):
	startTime = time.time()
	exploredStatesSet = set()
	fringeSet = set([initialState])
	visitedFromDict = {}
	heap = [(0, initialState)]
	nextLevelHeap = []
	depth = 0

	maxFringeSize = 0
	maxSearchDepth = 0

	while len(heap) > 0:
		mDistance, currentState = heapq.heappop(heap)
		
		if currentState in fringeSet:
			fringeSet.remove(currentState)

		if currentState.isGoalState():
			# we finished the puzzle
			endTime = time.time()

			output(visitedFromDict, initialState, currentState, len(exploredStatesSet), len(fringeSet),
				maxFringeSize, depth, depth, (endTime - startTime))
			return

		exploredStatesSet.add(currentState)

		connectedStates = currentState.getConnectedStates()
		for connectedState in connectedStates:
			if connectedState[0] not in fringeSet and connectedState[0] not in exploredStatesSet:
				connectedStateMDist = connectedState[0].heuristic() + depth + 1
				fringeSet.add(connectedState[0])
				visitedFromDict[connectedState[0]] = (currentState, connectedState[1])
				heapq.heappush(nextLevelHeap, (connectedStateMDist, connectedState[0]))

		if len(heap) == 0:
			heap = nextLevelHeap
			nextLevelHeap = []
			depth += 1

		if maxFringeSize < len(fringeSet):
			maxFringeSize = len(fringeSet)

	# if we reach this far in execution, the goal state is unobtainable
	print "unobtainable goal state"