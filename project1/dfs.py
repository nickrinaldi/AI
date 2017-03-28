from timeit import time
from game_state import GameState
from output import output

def dfsFindPath(initialState):
	startTime = time.time()
	exploredStatesSet = set()
	fringeSet = set([initialState])
	visitedFromDict = {}
	dfsStack = [(initialState, 0)]

	maxFringeSize = 0
	maxSearchDepth = 0

	while len(dfsStack) > 0:
		currentState, searchDepth = dfsStack.pop()
		
		if currentState in fringeSet:
			fringeSet.remove(currentState)
		
		if maxSearchDepth < searchDepth:
			maxSearchDepth = searchDepth

		if currentState.isGoalState():
			# we finished the puzzle
			endTime = time.time()

			output(visitedFromDict, initialState, currentState, len(exploredStatesSet), len(fringeSet),
				maxFringeSize, searchDepth, maxSearchDepth, (endTime - startTime))
			return

		exploredStatesSet.add(currentState)

		connectedStates = currentState.getConnectedStates()
		connectedStates.reverse()
		# reverse connectedStates to preserve UDLR visitation

		for connectedState in connectedStates:
			if connectedState[0] not in fringeSet and connectedState[0] not in exploredStatesSet:
				fringeSet.add(connectedState[0])
				visitedFromDict[connectedState[0]] = (currentState, connectedState[1])
				dfsStack.append((connectedState[0], searchDepth + 1))

		if maxFringeSize < len(fringeSet):
			maxFringeSize = len(fringeSet)

	# if we reach this far in execution, the goal state is unobtainable
	print "unobtainable goal state"