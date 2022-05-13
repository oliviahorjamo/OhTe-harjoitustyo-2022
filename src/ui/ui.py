
import pygame
from ui.gameloop import GameLoop

class UI:

    def __init__(self):
        display_height = 500
        display_width = 500
        pygame.init()
        display = pygame.display.set_mode((display_height, display_width))
        pygame.display.set_caption("Sudoku game")
        self.gameloop = GameLoop(display=display)
        self.start()

    def start(self):
        self.show_login_view()

    def show_login_view(self):
        self.gameloop.run()


ui = UI()
