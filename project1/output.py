from game_state import GameState

def output(visitedFromDict, initialState, goalState, nodesExpanded, fringeSize, maxFringeSize,
	searchDepth, maxSearchDepth, runningTime):
	path = []
	currentState = goalState

	while currentState != initialState:
		parentState = visitedFromDict[currentState]
		path.append(parentState[1])
		currentState = parentState[0]

	path.reverse()

	print "path_to_goal: ", path
	print "cost_of_path: ", len(path)
	print "nodes_expanded: ", nodesExpanded
	print "fringe_size: ", fringeSize
	print "max_fringe_size: ", maxFringeSize
	print "search_depth: ", searchDepth
	print "max_search_depth: ", maxSearchDepth
	print "running_time: ", runningTime
	return