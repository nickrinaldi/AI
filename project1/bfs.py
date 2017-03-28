from timeit import time
from game_state import GameState
from output import output
from Queue import Queue

def bfsFindPath(initialState):
	startTime = time.time()
	exploredSet = set()
	fringeSet = set([initialState])
	visitedByDict = {}
	frontierQueue = Queue()
	frontierQueue.put((initialState, 0))

	maxFringeSize = 0
	maxSearchDepth = 0

	while not frontierQueue.empty():
		currentState, searchDepth = frontierQueue.get()

		if currentState in fringeSet:
			fringeSet.remove(currentState)

		if maxSearchDepth < searchDepth:
			maxSearchDepth = searchDepth

		if currentState.isGoalState():
			endTime = time.time()
			output(visitedByDict, initialState, currentState, len(exploredSet), len(fringeSet),
				maxFringeSize, searchDepth, maxSearchDepth, (endTime - startTime))
			return

		exploredSet.add(currentState)

		connectedStates = currentState.getConnectedStates()
		for connectedState in connectedStates:
			if connectedState[0] not in fringeSet and connectedState[0] not in exploredSet:
				fringeSet.add(connectedState[0])
				visitedByDict[connectedState[0]] = (currentState, connectedState[1])
				frontierQueue.put((connectedState[0], searchDepth + 1))

		if maxFringeSize < len(fringeSet):
			maxFringeSize = len(fringeSet)

	# if we reach this far in execution, the goal state is unobtainable
	print "unobtainable goal state"