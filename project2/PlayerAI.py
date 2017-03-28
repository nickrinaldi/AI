import heapq
import time
from random import randint
from BaseAI import BaseAI
from Minimax import minimize, maximize
from StateEvaluator import evaluate

class PlayerAI(BaseAI):
	def getMove(self, grid):
		# init vars
		startTime = time.clock()
		exploredStates = {}
		depth = 1

		# print "evaluated grid: ", evaluate(grid)

		(alpha, beta) = (float("-inf"), float("inf"))
		moves = grid.getAvailableMoves()
		#bestMove = moves[randint(0, len(moves) - 1)] if moves else None
		bestMove = None
		timeout = False

		# IDDLS
		while not timeout and time.clock() - startTime < 0.08:
			(move, _, timeout) = maximize(grid, alpha, beta,
				exploredStates, depth, startTime)

			if not timeout:
				bestMove = move

			depth += 1

		# print "search depth: ", depth - 1
		# print "bestMove: ", bestMove
		# print "executionTime: ", time.clock() - startTime

		return bestMove
