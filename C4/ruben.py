from random import randrange


def column(grid: list, disc: str) -> int:
	grid_check = grid.copy()
	grid_check.pop(6)

	if grid[6] == [5, 5, 5, 5, 5, 5, 5, 5, 5]:
		print("DEBUG: TABLERO VACIO")
		return randrange(0, 9, 1)
	else:
		y_pos = 0
		for y in grid_check:
			x_pos = 0
			for x in y:
				if x != "_":
					if x != disc:
						if x_pos + 3 < grid[6][x_pos]:
							if grid[y_pos][x_pos + 3] == "_" or grid[y_pos][x_pos - 3] == "_":
								return x_pos + 3
						elif x_pos + 2 < grid[6][x_pos]:
							if grid[y_pos][x_pos + 2] == "_" or grid[y_pos][x_pos - 2] == "_":
								return x_pos + 2
						elif x_pos + 1 < grid[6][x_pos]:
							if grid[y_pos][x_pos + 1] == "_" or grid[y_pos][x_pos - 1] == "_":
								return x_pos + 1
							else:
								return randrange(0, 8, 1)
					else:
						if (x_pos == 8):
							if grid[6][x_pos] >= 0:
								return x_pos - 1
							else:
								return randrange(0, 8, 1)
						else:
							if grid[6][x_pos] >= 0:
								return x_pos + 1
							else:
								return randrange(0, 8, 1)
				x_pos = x_pos + 1
			y_pos = y_pos + 1
		return randrange(0, 8, 1)



