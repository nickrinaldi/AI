#!/usr/bin/python

import sys
import math
from ast import literal_eval
from game_state import GameState
from dfs import dfsFindPath
from bfs import bfsFindPath
from astSearch import astSearchFindPath

if (len(sys.argv) != 3) :
	print "incorrect arguments"
	sys.exit()

method = sys.argv[1]
initialStateTup = literal_eval(sys.argv[2])
dimension = int(math.sqrt(len(initialStateTup)))

initialState = GameState(initialStateTup, dimension)

if method == "dfs":
	dfsFindPath(initialState)
if method == "bfs":
	bfsFindPath(initialState)
if method == "ast":
	astSearchFindPath(initialState)
if method == "ida":
	bfsFindPath(initialState)
