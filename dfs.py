from game_state import GameState

def dfsFindPath(initialState):
	visitedStatesSet = set([initialState])
	visitedFromDict = {}
	dfsStack = [initialState]

	while len(dfsStack) > 0:
		currentState = dfsStack.pop()
		
		if currentState.isGoalState():
			# we finished the puzzle
			pathToGoal(visitedFromDict, initialState, currentState)
			return

		connectedStates = currentState.getConnectedStates()
		connectedStates.reverse()
		# reverse connectedStates to preserve UDLR visitation

		for connectedState in connectedStates:
			if connectedState[0] not in visitedStatesSet:
				visitedStatesSet.add(connectedState[0])
				visitedFromDict[connectedState[0]] = (currentState, connectedState[1])
				dfsStack.append(connectedState[0])

	# if we reach this far in execution, the goal state is unobtainable
	print "unobtainable goal state"


def pathToGoal(visitedFromDict, initialState, goalState):
	path = []
	currentState = goalState

	while currentState != initialState:
		parentState = visitedFromDict[currentState]
		path.append(parentState[1])
		currentState = parentState[0]

	path.reverse()
	print "path_to_goal: ", path
	return