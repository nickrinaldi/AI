import heapq
from timeit import time
from game_state import GameState
from output import output

def astSearchFindPath(initialState):
	startTime = time.time()
	exploredStatesSet = set()
	fringeSet = set([initialState])
	visitedFromDict = {}
	heap = [(0, initialState, 0)]

	maxFringeSize = 0
	maxSearchDepth = 0

	while len(heap) > 0:
		mDistance, currentState, searchDepth = heapq.heappop(heap)

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
			if connectedState[0] not in fringeSet and connectedState[0] not in exploredStatesSet:
				connectedStateMDist = connectedState[0].heuristic() + searchDepth + 1
				fringeSet.add(connectedState[0])
				visitedFromDict[connectedState[0]] = (currentState, connectedState[1])
				heapq.heappush(heap, (connectedStateMDist, connectedState[0], searchDepth + 1))

		if maxFringeSize < len(fringeSet):
			maxFringeSize = len(fringeSet)

	print "unobtainable goal state"