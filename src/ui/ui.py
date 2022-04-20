
import pygame
from ui.view_sudoku import ViewSudoku
from ui.gameloop import GameLoop
from ui.renderer import Renderer
from ui.view_login import LoginView
from ui.view_mainpage import Mainpage
from entities.sudoku import OriginalSudoku, Sudoku
from services.sudoku_service import sudoku_service
import ui.sprites

class UI:

    def __init__(self):
        #self.start()
        self.start_sudoku_view()

    def start(self):
        display_height = 200
        display_width = 200
        self.display = pygame.display.set_mode((display_width, display_height))

    def start_sudoku_view(self):
        original_sudoku = sudoku_service.find_original_numbers(1)
        sudoku = Sudoku(original_sudoku)
        cell_size = 33
        height = len(sudoku.grid)
        width = len(sudoku.grid[0])
        display_height = height * cell_size
        display_width = width * cell_size
        self.display = pygame.display.set_mode((display_width, display_height))
        view_sudoku = ViewSudoku(cell_size, sprites = ui.sprites, sudoku = sudoku, original_sudoku = original_sudoku)
        renderer = Renderer(self.display, view_sudoku)
        game_loop = GameLoop(view_sudoku, cell_size, renderer)
        game_loop.start()

