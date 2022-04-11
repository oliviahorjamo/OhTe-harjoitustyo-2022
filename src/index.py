# Tää tiedosto pyörittää aluksi koko hommaa / starttaa sovelluksen

import pygame
from entities.sudoku import OriginalSudoku, Sudoku
from ui.view_sudoku import ViewSudoku
from ui.view_sudoku import GameLoop
from ui.view_sudoku import Renderer
import ui.sprites


def main():
    cell_size = 33

    original_sudoku = OriginalSudoku(1)
    sudoku = Sudoku(1)
    height = len(sudoku.grid)
    width = len(sudoku.grid[0])
    display_height = height * cell_size
    display_width = width * cell_size
    display = pygame.display.set_mode((display_width, display_height))
    view_sudoku = ViewSudoku(
    cell_size, sprites=ui.sprites, sudoku=sudoku, original=original_sudoku)
    renderer = Renderer(display, view_sudoku)
    game_loop = GameLoop(view_sudoku, cell_size, renderer)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
