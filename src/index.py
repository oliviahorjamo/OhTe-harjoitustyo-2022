#Tää tiedosto pyörittää aluksi koko hommaa / starttaa sovelluksen

from entities.sudoku import Sudoku
from ui.view_sudoku import ViewSudoku
from ui.view_sudoku import GameLoop
from ui.view_sudoku import Renderer
import ui.sprites
import pygame

def main():

    cell_size = 33

    sudoku = Sudoku(1)

    height = len(sudoku.grid)
    width = len(sudoku.grid[0])
    display_height = height * cell_size
    display_width = width * cell_size
    display = pygame.display.set_mode((display_width, display_height))
    view_sudoku = ViewSudoku(cell_size, sprites = ui.sprites, sudoku = sudoku)
    renderer = Renderer(display, view_sudoku)
    game_loop = GameLoop(view_sudoku, cell_size, renderer)
    
    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
