import heapq
import math
import time
from StateEvaluator import evaluate

# TODO: check to make sure we don't visit states multiple times

def minimize(grid, alpha, beta, depth, startTime):

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
			# get the evaulated value of the child state
			(_, childUtility, timeout) = maximize(child, alpha, beta, depth - 1, startTime)

			if timeout:
				return (minUtility, True)

			if childUtility < minUtility:
				minUtility = childUtility

			if alpha >= minUtility:
				# pruning the rest of the branches
				break

			if beta > minUtility:
				beta = minUtility

	return (minUtility, False)

def maximize(grid, alpha, beta, depth, startTime):

	availableMoves = grid.getAvailableMoves()
	# terminal test
	if not depth or not availableMoves:
		# is terminal
		return (None, evaluate(grid), False)

	# if we are out of time
	if time.clock() - startTime > 0.08:
		return (None, grid.getMaxTile(), True)

	(bestMove, maxUtility) = (None, float("-inf"))

	for move in availableMoves:
		# get the current child
		child = grid.clone()
		child.move(move)
		# get the evaulated value of the child state
		(childUtility, timeout) = minimize(child, alpha, beta, depth - 1, startTime)

		if timeout:
			return (None, maxUtility, True)

		if childUtility > maxUtility:
				maxUtility = childUtility
				bestMove = move

		if maxUtility >= beta:
			# pruning the rest of the branches
			break

		if maxUtility > alpha:
			alpha = maxUtility

	return (bestMove, maxUtility, False)