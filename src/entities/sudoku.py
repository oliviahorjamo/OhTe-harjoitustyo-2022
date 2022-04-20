#from services.sudoku_service import sudoku_service

class OriginalSudoku:
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid
        #self.grid = [
         #   [7, 8, 0, 4, 0, 0, 1, 2, 0],
          #  [6, 0, 0, 0, 7, 5, 0, 0, 9],
          #  [0, 0, 0, 6, 0, 1, 0, 7, 8],
          #  [0, 0, 7, 0, 4, 0, 2, 6, 0],
          #  [0, 0, 1, 0, 5, 0, 9, 3, 0],
          #  [9, 0, 4, 0, 6, 0, 0, 0, 5],
          #  [0, 7, 0, 3, 0, 0, 0, 1, 2],
          #  [1, 2, 0, 0, 0, 7, 4, 0, 0],
          #  [0, 4, 9, 2, 0, 6, 0, 0, 7]
        #]


class Sudoku():
    def __init__(self, original_sudoku):
        self.original_sudoku = original_sudoku
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
