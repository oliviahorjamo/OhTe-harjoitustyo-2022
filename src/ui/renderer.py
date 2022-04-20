import pygame
from ui.view_sudoku import view_sudoku

class Renderer:
    def __init__(self, display):
        print(display)
        self._display = display
        self.view_sudoku = view_sudoku

    def render_sudoku(self):
        self._display.fill((255, 255, 255))
        self.view_sudoku.all_sprites.draw(self._display)


        #nyt nää piirretään automaattisesti mut pitäis jotenkin saada niin että
        #piirtää vaan jos ollaan view_sudoku kohdassa
        self.view_sudoku.draw_original_numbers(self._display)
        self.view_sudoku.draw_added_numbers(self._display)
        self.view_sudoku.draw_lines(self._display)
        self.view_sudoku.draw_selected_square()

        pygame.display.update()

    def render_mainpage(self):
        #Mainpagessa pitäis piirtää kaikki näppäimet
        self._display.fill((255,255,255))
        pygame.display.update()