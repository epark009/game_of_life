import random
import copy

class Grid:
	"""
	Handles the grid for Conway's Game of Life.
	Is the model for this program.
	"""
	
	def __init__(self, grid_size):
		self.grid = []
		self.width = grid_size[0]
		self.height = grid_size[1]
		for x in range(self.width):
			self.grid.append([])
			for y in range(self.height):
				self.grid[x].append(False)

	def get(self, x, y):
		"""
		returns x,y coordinate of grid
		"""
		return self.grid[x][y]

	def randomize_cells(self, num_cells):
		"""
		randomly selects items in the grid
		"""
		for i in range(num_cells):
			try:
				self.grid[random.choice(range(self.width))][random.choice(range(self.height))] = True
			except IndexError:
				pass

	def update_cells(self):
		"""
		uses the game of life algorithm to determine what the grid should look like next
		"""
		grid_copy = copy.deepcopy(self.grid)
		
		for x in range(len(self.grid)):
			for y in range(len(self.grid[x])):
				neighbors = self.get_neighbors(x, y)
				num_neighbors = len([n for n in neighbors if n])
				if self.grid[x][y]:
					if num_neighbors < 2 or num_neighbors > 3:
						grid_copy[x][y] = False
				else:
					if num_neighbors == 3:
						grid_copy[x][y] = True
						
		for x in range(len(self.grid)):
			for y in range(len(self.grid[x])):
				self.grid[x][y] = grid_copy[x][y]

	def get_neighbors(self, x, y):
		"""
		gets the neighboring cells in a selected coordinate of the grid
		returns as a list of true or falses
		"""
		if x == 0:
			left = self.width - 1
		else:
			left = x - 1

		if x == self.width - 1:
			right = 0
		else:
			right = x + 1

		if y == 0:
			top = self.height - 1
		else:
			top = y - 1

		if y == self.height - 1:
			bottom = 0
		else:
			bottom = y + 1

		return [
			self.grid[left][top],
			self.grid[x][top],
			self.grid[right][top],
			self.grid[right][y],
			self.grid[right][bottom],
			self.grid[x][bottom],
			self.grid[left][bottom],
			self.grid[left][y]
		]
