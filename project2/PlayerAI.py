import heapq
import time
from random import randint
from BaseAI import BaseAI
from Minimax import minimize, maximize

class PlayerAI(BaseAI):
	def getMove(self, grid):
		# init vars
		startTime = time.clock()
		depth = 1

		(alpha, beta) = (float("-inf"), float("inf"))
		moves = grid.getAvailableMoves()
		#bestMove = moves[randint(0, len(moves) - 1)] if moves else None
		bestMove = None

		# IDDLS
		while time.clock() - startTime < 0.08:
			(move, _, timeout) = maximize(grid, alpha, beta, depth, startTime)

			if not timeout:
				bestMove = move

			depth += 1

		# print "bestMove: ", bestMove
		# print "executionTime: ", time.clock() - startTime

		return bestMove
