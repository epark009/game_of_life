import pygame
import random

class Canvas:
	"""
	Draws the grid and animates it using pygame.
	This is the view of the program.
	"""
	def __init__(self, window_size, cell_size, grid_size, fps, animation):
		self.screen = pygame.display.set_mode(window_size)
		pygame.display.set_caption("Conway's Game of Life")
		self.surface = pygame.Surface(self.screen.get_size()).convert()

		self.cell_size = cell_size
		self.current_cell_size = cell_size
		self.speed = 50/fps
		if self.speed == 0:
			self.speed = 1
			
		self.themes = ["black and white", "blue and orange", "red and green", "purple and yellow"]
		self.theme = random.choice(self.themes)
		self.theme_change_buffer = 8
				
		if self.theme == "black and white":
			self.background = [75, 75, 75]
			self.color = [255, 255, 255]
		elif self.theme == "blue and orange":
			self.background = [30, 30, 75]
			self.color = [255, 127, 0]
		elif self.theme == "red and green":
			self.background = [75, 0, 0]
			self.color = [0, 255, 0]
		elif self.theme == "purple and yellow":
			self.background = [75, 30, 75]
			self.color = [255, 255, 0]
			
		self.animation = animation
		
	def draw_grid(self, grid, reset):
		"""
		draws the grid and animates it
		randomly selects themes too
		"""
		if self.animation:
			if reset:
				if self.theme_change_buffer <= 0 and random.random() > 0.8:
					self.theme = random.choice(self.themes)
					self.theme_change_buffer = 8
				else:
					self.theme_change_buffer -= 1
					
				if self.theme == "black and white":
					self.background = [75, 75, 75]
					self.color = [255, 255, 255]
				elif self.theme == "blue and orange":
					self.background = [30, 30, 75]
					self.color = [255, 127, 0]
				elif self.theme == "red and green":
					self.background = [75, 0, 0]
					self.color = [0, 255, 0]
				elif self.theme == "purple and yellow":
					self.background = [75, 30, 75]
					self.color = [255, 255, 0]
					
				self.current_cell_size = self.cell_size/2
				if self.current_cell_size == 0:
					self.current_cell_size = 1
					
			else:
				if self.theme == "black and white":
					self.background[0] = self.background[1] = self.background[2] = self.background[0] - self.speed
				elif self.theme == "blue and orange":
					self.background[2] -= self.speed
					if self.background[2] < 30:
						self.background[0] = self.background[1] = self.background[0] - self.speed
				elif self.theme == "red and green":
					self.background[0] -= self.speed
				elif self.theme == "purple and yellow":
					self.background[0] = self.background[2] = self.background[0] - self.speed
					if self.background[0] < 30:
						self.background[1] -= self.speed
						
				self.current_cell_size += self.speed
				if self.current_cell_size > self.cell_size:
					self.current_cell_size = self.cell_size
		else:
			self.background = [15, 15, 15]
			self.color = [255, 255, 255]
			self.current_cell_size = self.cell_size
					
		self.surface.fill(tuple(self.background))
		self.screen.blit(self.surface, (0, 0))
		
		for x in range(grid.width):
			for y in range(grid.height):
				if grid.get(x, y):
					pygame.draw.circle(self.screen, self.color, [x * self.cell_size, y * self.cell_size], self.current_cell_size/2)

		pygame.display.flip()
