class GameState:

	def __init__(self, gameStateTuple, dimension):
		self.state = gameStateTuple
		self.dimension = dimension
		self.emptyPosition = -1;

		for index in range(len(gameStateTuple)):
			if gameStateTuple[index] == 0:
				self.emptyPosition = index

	# if we are done with our puzzle, return True. Else return False.
	def isGoalState(self):
		for index in range(1, len(self.state)):
			if self.state[index - 1] > self.state[index]:
				# if the left element is larger than the right element
				# we are not at the goal state
				return False

		return True

	def getConnectedStates(self):
		connectedStates = [];
		
		if self.emptyPosition - self.dimension >= 0:
			# we can move the tile above, down
			connectedStateTuple = self.state
			connectedStateTuple[self.emptyPosition] = connectedStateTuple[self.emptyPosition - self.dimension]
			connectedStateTuple[self.emptyPosition - self.dimension] = 0
			connectedStates.append(GameState(connectedStateTuple, self.dimension))

		if (self.emptyPosition + 1) % self.dimension != 0:
			# we can move the tile to the right, left
			connectedStateTuple = self.state
			connectedStateTuple[self.emptyPosition] = connectedStateTuple[self.emptyPosition + 1]
			connectedStateTuple[self.emptyPosition + 1] = 0
			connectedStates.append(GameState(connectedStateTuple, self.dimension))

		if self.emptyPosition % self.dimension != 0:
			# we can move the tile to the left, right
			connectedStateTuple = self.state
			connectedStateTuple[self.emptyPosition] = connectedStateTuple[self.emptyPosition - 1]
			connectedStateTuple[self.emptyPosition - 1] = 0
			connectedStates.append(GameState(connectedStateTuple, self.dimension))

		if self.emptyPosition + self.dimension >= len(self.state):
			# we can move the tile underneath, up
			connectedStateTuple = self.state
			connectedStateTuple[self.emptyPosition] = connectedStateTuple[self.emptyPosition + self.dimension]
			connectedStateTuple[self.emptyPosition + self.dimension] = 0
			connectedStates.append(GameState(connectedStateTuple, self.dimension))

		return connectedStates