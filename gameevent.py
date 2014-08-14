import pygame

class GameEvent:
	def __init__(self, update_event_id, fps, update_rate):
		"""
		Reads events and tells program when to update.
		This is the controller of the program.
		"""
		self.update_event_id = update_event_id
		self.fps = fps
		self.update_rate = update_rate
		self.clock = pygame.time.Clock()
		
		pygame.time.set_timer(self.update_event_id, self.update_rate)
		
	def run(self):
		"""
		reads events and keeps track of time
		"""
		message = "none"
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				message = "quit"
			elif event.type == self.update_event_id:
				message = "update grid"
				
		self.clock.tick(self.fps)
		
		return message
