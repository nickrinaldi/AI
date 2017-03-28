from Grid       	import Grid
from Displayer  	import Displayer
from StateEvaluator	import evaluate

grid = Grid(4)
displayer = Displayer()

grid.insertTile((0, 0), 32)
grid.insertTile((1, 0), 16)
grid.insertTile((2, 0), 8)
grid.insertTile((3, 0), 4)
grid.insertTile((2, 1), 2)
grid.insertTile((3, 1), 4)
grid.insertTile((3, 2), 4)

displayer.display(grid)
print "evalation: ", evaluate(grid)