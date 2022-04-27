
import pygame
from ui.view_sudoku import ViewSudoku
from ui.gameloop import GameLoop
from ui.renderer import Renderer
from ui.view_login import login_view
from ui.view_mainpage import mainpage
from entities.sudoku import OriginalSudoku, Sudoku
from services.sudoku_service import sudoku_service
import ui.sprites


class UI:

    def __init__(self):
        self.gameloop = GameLoop()

        self.start()

    def start(self):
        self.show_login_view()

    def show_login_view(self):
        self.gameloop._renderer.current_view = login_view
        self.gameloop.show_login = True
        self.gameloop.run()

ui = UI()
