#!/usr/bin/python

import sys
import math
from ast import literal_eval
from game_state import GameState
from bfs import findPath

if (len(sys.argv) != 3) :
	print "incorrect arguments"
	sys.exit()

method = sys.argv[1]
initialStateTup = literal_eval(sys.argv[2])
dimension = int(math.sqrt(len(initialStateTup)))

initialState = GameState(initialStateTup, dimension)
findPath(initialState)

# connectedStates = initialGameState.getConnectedStates()
# for index in range(len(connectedStates)):
# 	print connectedStates[index]