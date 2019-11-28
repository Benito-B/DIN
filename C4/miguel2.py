from random import randrange
def myName():
	return "Miguel"

def column(grid:list,disc:str) ->int:

	#input()



	for a in range(len(grid)):##revisar horizontalmente
		for b in range(len(grid[a])):
			if (a<6):


				for z in range(0,6):##revisa 3 seguidas
					y = z + 1
					x = z + 2

					if (grid[a][z] == "#" and grid[a][y] == "#" and grid[a][x] == "#" and grid[a][z + 3] == "_"):
						return z + 3

					if (grid[a][z] == "@"  and grid[a][y] == "@" and grid[a][x] == "@" and grid[a][z+3] == "_"):
						return z+3


				for j in range(8,3,-1):##revisa 3 seguidad decendentemente

					h = j - 1
					i = j - 2
					if (grid[a][j] == "#" and grid[a][h] == "#" and grid[a][i] == "" and grid[a][j-3] == "_"):
						return j-3

					if (grid[a][j] == "@" and grid[a][h] == "@" and grid[a][i] == "@" and grid[a][j-3] == "_"):
						return j-3

				for b in range(0,5):##revisa que no haya un hueco entre dos iguales
					c=b+1
					d=b+3
					e=b+4

					if (grid[a][b] == "#" and grid[a][c] == "#" and grid[a][d] == "#" and grid[a][e] == "#" and grid[a][b+2]=="_"):
						return b+2

					if (grid[a][b] == "@" and grid[a][c] == "@" and grid[a][d] == "@" and grid[a][e] == "@" and grid[a][b+2]=="_"):
						return b+2

				for m in range(0,6):##revisa que no haya dos iguales , hueco y otra igual(asendentemente)
					l=m+1
					p=m+3

					if (grid[a][m] == "#" and grid[a][l] == "#" and grid[a][p] == "#" and grid[a][l+2]=="_"):
						return l+2

					if (grid[a][m] == "@" and grid[a][l] == "@" and grid[a][p] == "@" and grid[a][l+2]=="_"):
						return l+2


				for m in range(8,3,-1):##revisa que no haya dos iguales , hueco y otra igual(desendentemente)

					l = m - 1
					p = m - 3
					if (grid[a][m] == "#" and grid[a][l] == "#" and grid[a][p] == "#" and grid[a][l - 2] == "_"):
						return l -2

					if (grid[a][m] == "@" and grid[a][l] == "@" and grid[a][p] == "@" and grid[a][l - 2] == "_"):
						return l - 2





	return randrange(0, 9, 1)




