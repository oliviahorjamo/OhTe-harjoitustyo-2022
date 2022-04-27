import pygame
from ui.view_login import LoginView
from ui.view_mainpage import Mainpage
from ui.view_sudoku import ViewSudoku
from ui import ui

class Renderer:
    def __init__(self, display, current_view = None):
        self._display = display
        self.current_view = current_view

    def render(self):
        self._display.fill((255, 255, 255))
        if isinstance(self.current_view, LoginView):
            self.current_view.draw_login_view()
        elif isinstance(self.current_view, Mainpage):
            self.current_view.draw_mainpage(self._display)
        elif isinstance(self.current_view, ViewSudoku):
            self.current_view.all_sprites.draw(self._display)
            self.current_view.draw_sudoku(self._display)

        pygame.display.update()