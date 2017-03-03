class GameState(object):

	def __init__(self, gameStateTuple, dimension):
		self.state = gameStateTuple
		self.dimension = dimension
		self.emptyPosition = -1;

		for index in range(len(gameStateTuple)):
			if gameStateTuple[index] == 0:
				self.emptyPosition = index

		self.frozen = True

	def __setattr__(self, name, value):
		if getattr(self, 'frozen', False):
			raise AttributeError('Attempt to modify immutable object')
		super(GameState, self).__setattr__(name, value)

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
			connectedStateTuple = (self.state[0:self.emptyPosition - self.dimension] +
				(0,) + self.state[self.emptyPosition - self.dimension + 1:self.emptyPosition] +
				(self.state[self.emptyPosition - self.dimension],) + self.state[self.emptyPosition + 1:])

			connectedStates.append((GameState(connectedStateTuple, self.dimension), 'Up'))

		if self.emptyPosition + self.dimension < len(self.state):
			# we can move the tile underneath, up
			connectedStateTuple = (self.state[0:self.emptyPosition] + (self.state[self.emptyPosition + self.dimension],) +
				self.state[self.emptyPosition + 1:self.emptyPosition + self.dimension] + (0,))

			if self.emptyPosition + self.dimension + 1 < len(self.state):
				connectedStateTuple = connectedStateTuple + self.state[self.emptyPosition + self.dimension + 1:]

			connectedStates.append((GameState(connectedStateTuple, self.dimension), 'Down'))

		if self.emptyPosition % self.dimension != 0:
			# we can move the tile to the left, right
			connectedStateTuple = (self.state[0:self.emptyPosition - 1] + (0,) + (self.state[self.emptyPosition - 1],) +
				self.state[self.emptyPosition + 1:])

			connectedStates.append((GameState(connectedStateTuple, self.dimension), 'Left'))

		if (self.emptyPosition + 1) % self.dimension != 0:
			# we can move the tile to the right, left
			connectedStateTuple = (self.state[0:self.emptyPosition] + (self.state[self.emptyPosition + 1],) +
				(0,) + self.state[self.emptyPosition + 2:])

			connectedStates.append((GameState(connectedStateTuple, self.dimension), 'Right'))

		return connectedStates

	def __repr__(self):
		return "GameState%s" % str(self.state)

	def __eq__(self, other):
		if isinstance(other, GameState):
			return (self.state == other.state)
		else:
			return False

	def __ne__(self, other):
		return (not self.__eq__(other))

	def __hash__(self):
		return hash(self.state)

	def heuristic(self):
		# manhattan distance
		totalDistance = 0

		for index in range(len(self.state)):
			if self.state[index] != index and self.state[index] != 0:
				xDistance = abs((self.state[index] % self.dimension) -
					(index % self.dimension))
				yDistance = abs((self.state[index] // self.dimension) -
					(index // self.dimension))
				totalDistance += (xDistance + yDistance)

		return totalDistance

	def __cmp__(self, other):
		return cmp(self.heuristic(), other.heuristic())