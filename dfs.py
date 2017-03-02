from game_state import GameState

def dfsFindPath(initialState):
	exploredStatesSet = set()
	frontierStatesSet = set([initialState])
	visitedFromDict = {}
	dfsStack = [initialState]

	while len(dfsStack) > 0:
		currentState = dfsStack.pop()
		exploredStatesSet.add(currentState)

		if currentState in frontierStatesSet:
			frontierStatesSet.remove(currentState)
		
		if currentState.isGoalState():
			# we finished the puzzle
			pathToGoal(visitedFromDict, initialState, currentState)
			print "nodes_expanded: ", len(exploredStatesSet)
			return

		connectedStates = currentState.getConnectedStates()
		connectedStates.reverse()
		# reverse connectedStates to preserve UDLR visitation

		for connectedState in connectedStates:
			if connectedState[0] not in frontierStatesSet and connectedState[0] not in exploredStatesSet:
				frontierStatesSet.add(connectedState[0])
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