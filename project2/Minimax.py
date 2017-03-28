import heapq
import math
import time
from StateEvaluator import evaluate

# TODO: check to make sure we don't visit states multiple times

def minimize(grid, alpha, beta, exploredStates, depth, startTime):

	emptyCells = grid.getAvailableCells()
	possibleNewTiles = [2, 4]
	# terminal test
	if not depth or not emptyCells:
		# is terminal
		return (evaluate(grid), False)

	if time.clock() - startTime > 0.08:
		return (None, True)

	minUtility = float("inf")

	# explore all available children
	for emptyCell in emptyCells:
		for possibleNewTile in possibleNewTiles:
			# get the current child
			child = grid.clone()
			child.insertTile(emptyCell, possibleNewTile)

			childUtility = None

			if child not in exploredStates:

				# get the evaulated value of the child state
				(_, childUtility, timeout) = maximize(child, alpha, beta,
					exploredStates, depth - 1, startTime)

				if timeout:
					return (None, True)

				exploredStates[child] = childUtility
			
			else:
				childUtility = exploredStates[child]
				print "we've explored this state before"

			if childUtility < minUtility:
				minUtility = childUtility

			if alpha >= minUtility:
				# pruning the rest of the branches
				break

			if beta > minUtility:
				beta = minUtility

	return (minUtility, False)

def maximize(grid, alpha, beta, exploredStates, depth, startTime):

	availableMoves = grid.getAvailableMoves()
	# terminal test
	if not depth or not availableMoves:
		# is terminal
		return (None, evaluate(grid), False)

	# if we are out of time
	if time.clock() - startTime > 0.08:
		return (None, None, True)

	(bestMove, maxUtility) = (None, float("-inf"))

	for move in availableMoves:
		# get the current child
		child = grid.clone()
		child.move(move)

		childUtility = None

		if child not in exploredStates:

			# get the evaulated value of the child state
			(childUtility, timeout) = minimize(child, alpha, beta,
				exploredStates, depth - 1, startTime)

			if timeout:
				return (None, maxUtility, True)

			exploredStates[child] = childUtility

		else:
			childUtility = exploredStates[child]
			print "we've explored this state before"

		if childUtility > maxUtility:
				maxUtility = childUtility
				bestMove = move

		if maxUtility >= beta:
			# pruning the rest of the branches
			break

		if maxUtility > alpha:
			alpha = maxUtility

	return (bestMove, maxUtility, False)