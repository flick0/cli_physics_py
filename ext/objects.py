
__shapes__ = [
    'circle',
    'rect',
    'empty'
]


from pyparsing import empty


class Geometry:
    def __init__(self,shape:str):
        if shape not in __shapes__:
            raise Exception("Shape not found")
        self.shape = shape
        self.size = (1,1)
        if self.shape == 'circle':
            self.emoji = "o"
        elif self.shape == 'rect':
            self.emoji = "x"
        elif self.shape == "empty":
            self.emoji = "-"

    
    def to_dict(self):
        return {
            'shape': self.shape,
            'size': self.size
        }

class Cell:
    def __init__(self,geometry:Geometry,pos:tuple):
        self.geometry = geometry
        self.color = '#FFFFFF'
        self.pos = (0,0)
        self.x = pos[0]
        self.y = pos[1]
    
    def to_dict(self):
        return {
            'geometry': self.geometry.to_dict(),
            'color': self.color
        }

class Board:
    def __init__(self,size:tuple=(0,0)) -> None:
        self.cells = []
        self.size = size
    
    def add_cell(self,cell:Cell) -> None:
        self.cells.append(cell)
    
    def to_dict(self):
        return {
            'size': self.size,
            'cells': [cell.to_dict() for cell in self.cells]
        }
    
    def parse(self):
        board = {}
        for x in range(self.size[0]):
            board[x] = []
            for y in range(self.size[1]):
                board[x].append(Cell(Geometry('empty'),(x,y)))
        for cell in self.cells:
            board[cell.x][cell.y] = cell
        return board
    
    def render(self):
        board = self.parse()
        rend = ""
        for x in board.values():
            for cell in x:
                rend +=cell.geometry.emoji
            rend += "\n"
        return rend
