import pygame
import grid as g
import gameevent as e
import canvas as c

def main():
	"""
	Conway's Game of Life.
	Now with sweet colors and animation!
	"""
	
	(width, height) = (800, 600)
	cell_size = 16
	fps = 60
	update_rate = 500
	update_event_id = 24
	animation = True
	starting_cells = 1000

	try:
		f = open("init.txt", 'r')
		for line in f:
			param = line.split("=")
			if param[0] == "width":
				width = int(param[1])
			elif param[0] == "height":
				height = int(param[1])
			elif param[0] == "cellsize":
				cell_size = int(param[1])
			elif param[0] == "fps":
				fps = int(param[1])
			elif param[0] == "updaterate":
				update_rate = int(param[1])
			elif param[0] == "animation":
				if int(param[1]) == 0:
					animation = False
				else:
					animation = True
			elif param[0] == "startingcells":
				starting_cells = int(param[1])
	except:
		f = open("init.txt", "w")
		f.write(
			"width=800\n" +
			"height=600\n" +
			"cellsize=16\n" +
			"fps=60\n" +
			"updaterate=500\n" +
			"animation=1\n" +
			"startingcells=1000\n"
		)
	
	grid_size = (width/cell_size, height/cell_size)
	grid = g.Grid(grid_size)
	canvas = c.Canvas((width, height), cell_size, grid_size, fps, animation)
	events = e.GameEvent(update_event_id, fps, update_rate)
	
	message = "none"
				

	grid.randomize_cells(starting_cells)

	pygame.init()

	# main game loop
	while message != "quit":
		message = events.run()
		
		if message == "update grid":
			grid.update_cells()
			canvas.draw_grid(grid, True)
			grid.randomize_cells(1)
		else:
			canvas.draw_grid(grid, False)

if __name__ == "__main__":
	main()
