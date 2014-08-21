import pygame

class GameEvent:
	def __init__(self, update_event_id, fps, update_rate, grid, canvas):
		"""
		Reads events and tells program when to update.
		This is the controller of the program.
		"""
		self.update_event_id = update_event_id
		self.fps = fps
		self.update_rate = update_rate
		self.clock = pygame.time.Clock()
		self.paused = False
		self.grid = grid
		self.canvas = canvas

		self.mouse_drag_mode = ""
		
		pygame.time.set_timer(self.update_event_id, self.update_rate)
		
	def run(self):
		"""
		reads events and keeps track of time
		"""
		message = "none"
		params = []

		mouse_pos = pygame.mouse.get_pos()
		mouse_x = mouse_pos[0] / self.canvas.cell_size
		mouse_y = mouse_pos[1] / self.canvas.cell_size
		params.append(mouse_x)
		params.append(mouse_y)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				message = "quit"
			elif event.type == self.update_event_id:
				message = "update grid"
			elif event.type == pygame.KEYDOWN:
				if pygame.key.get_pressed()[pygame.K_SPACE]:
					if self.paused:
						message = "resume"
						self.paused = False
					else:
						message = "pause"
						self.paused = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if self.grid.get(mouse_x, mouse_y):
					self.mouse_drag_mode = "removing"
				else:
					self.mouse_drag_mode = "placing"
			elif event.type == pygame.MOUSEBUTTONUP:
				self.mouse_drag_mode = ""

		if self.mouse_drag_mode == "removing":
			message = "remove cell"
		elif self.mouse_drag_mode == "placing":
			message = "place cell"
				
		self.clock.tick(self.fps)
		
		return message, params
