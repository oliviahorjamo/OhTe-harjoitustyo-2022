import pygame

class Renderer:
    def __init__(self, display, view_sudoku):
        self._display = display
        self.view_sudoku = view_sudoku

    def render(self):
        self._display.fill((255, 255, 255))
        self.view_sudoku.all_sprites.draw(self._display)


        #nyt nää piirretään automaattisesti mut pitäis jotenkin saada niin että
        #piirtää vaan jos ollaan view_sudoku kohdassa
        self.view_sudoku.draw_original_numbers()
        self.view_sudoku.draw_added_numbers()
        self.view_sudoku.draw_lines()
        self.view_sudoku.draw_selected_square()

        pygame.display.update()