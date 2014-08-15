import pygame
import random

class Canvas:
	"""
	Draws the grid and animates it using pygame.
	This is the view of the program.
	"""
	def __init__(self, window_size, cell_size, grid_size):
		self.screen = pygame.display.set_mode(window_size)
		pygame.display.set_caption("Conway's Game of Life")
		self.surface = pygame.Surface(self.screen.get_size()).convert()

		self.cell_size = cell_size
				
		self.background = [15, 15, 15]
		self.color = [255, 255, 255]
		
	def draw_grid(self, grid, reset):
		"""
		draws the grid
		"""
		self.surface.fill(tuple(self.background))
		self.screen.blit(self.surface, (0, 0))
		
		for x in range(grid.width):
			for y in range(grid.height):
				if grid.get(x, y):
					pygame.draw.circle(self.screen, self.color, [x * self.cell_size, y * self.cell_size], self.cell_size/2)

		pygame.display.flip()
