import heapq
from timeit import time
from game_state import GameState
from output import output

def astSearchFindPath(initialState):
	startTime = time.time()
	exploredStatesSet = set()
	fringeSet = set([initialState])
	visitedFromDict = {}
	heap = [(initialState, 0)]

	maxFringeSize = 0
	maxSearchDepth = 0

	while len(heap) > 0:
		currentState, searchDepth = heapq.heappop(heap)

		if currentState in fringeSet:
			fringeSet.remove(currentState)

		if maxSearchDepth < searchDepth:
			maxSearchDepth = searchDepth

		if currentState.isGoalState():
			endTime = time.time()
			output(visitedFromDict, initialState, currentState, len(exploredStatesSet), len(fringeSet),
				maxFringeSize, searchDepth, maxSearchDepth, (endTime - startTime))
			return

		exploredStatesSet.add(currentState)

		connectedStates = currentState.getConnectedStates()
		for connectedState in connectedStates:
			mDistance = connectedState[0].heuristic()
			if mDistance < currentState.heuristic():
				fringeSet.add(connectedState[0])
				visitedFromDict[connectedState[0]] = (currentState, connectedState[1])
				heapq.heappush(heap, (connectedState[0], searchDepth + 1))

		if maxFringeSize < len(fringeSet):
			maxFringeSize = len(fringeSet)

	print "unobtainable goal state"