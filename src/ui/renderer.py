import pygame
#from ui.view_sudoku import view_sudoku
from ui.view_mainpage import mainpage

class Renderer:
    def __init__(self, display, view_sudoku = None):
        self._display = display
        self.mainpage = mainpage
        self.view_sudoku = view_sudoku

    def render_sudoku(self):
        self._display.fill((255, 255, 255))
        self.view_sudoku.all_sprites.draw(self._display)

        self.view_sudoku.draw_original_numbers(self._display)
        self.view_sudoku.draw_added_numbers(self._display)
        self.view_sudoku.draw_lines(self._display)
        self.view_sudoku.draw_selected_square()

        pygame.display.update()

    def render_mainpage(self):
        #olisko kaikki piirtämiset parempi tehä gameloopissa?
        self._display.fill((255,255,255))
        self.mainpage.draw_text(self._display)
        self.mainpage.draw_sudoku_list(self._display)
        pygame.display.update()