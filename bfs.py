from game_state import GameState
from dfs import pathToGoal
from Queue import Queue

def bfsFindPath(initialState):
	visitedStatesSet = set([initialState])
	visitedFromDict = {}
	frontierQueue = Queue()
	frontierQueue.put(initialState)

	while not frontierQueue.empty():
		currentState = frontierQueue.get()

		if currentState.isGoalState():
			pathToGoal(visitedFromDict, initialState, currentState)
			return

		connectedStates = currentState.getConnectedStates()
		
		for connectedState in connectedStates:
			if connectedState[0] not in visitedStatesSet:
				visitedStatesSet.add(connectedState[0])
				visitedFromDict[connectedState[0]] = (currentState, connectedState[1])
				frontierQueue.put(connectedState[0])

	# if we reach this far in execution, the goal state is unobtainable
	print "unobtainable goal state"