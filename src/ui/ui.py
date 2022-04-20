
import pygame
from ui.view_sudoku import view_sudoku
from ui.gameloop import GameLoop
from ui.renderer import Renderer
from ui.view_login import LoginView
from ui.view_mainpage import Mainpage
from entities.sudoku import OriginalSudoku, Sudoku
from services.sudoku_service import sudoku_service
import ui.sprites

class UI:

    def __init__(self):
        self.mainpage = Mainpage()
        self.view_sudoku = view_sudoku
        
        self.start()
        self.start_sudoku_view()

    def start(self):
        self.gameloop = GameLoop()
        #self.gameloop.start()
        

    def start_sudoku_view(self):
        self.gameloop = GameLoop()
        self.gameloop.start_sudoku_view()

