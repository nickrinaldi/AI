#!/usr/bin/python

import sys
import math
from ast import literal_eval
from game_state import GameState

if (len(sys.argv) != 3) :
	print "incorrect arguments"
	sys.exit()

method = sys.argv[1]
initialStateTup = literal_eval(sys.argv[2])
dimension = int(math.sqrt(len(initialStateTup)))

initialGameState = GameState(initialStateTup, dimension)
print "is completed: %s" % initialGameState.isGoalState()