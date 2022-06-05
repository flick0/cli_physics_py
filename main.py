from ext.objects import *

board = Board((10,20))
board.add_cell(Cell(Geometry('circle'),(5,10)))

print(board.render())