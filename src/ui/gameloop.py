import pygame
from ui.clock import Clock
from ui.renderer import Renderer

class GameLoop:

    def __init__(self, view_sudoku, cell_size, renderer):
        self._renderer = renderer
        self.clock = Clock()
        self._cell_size = cell_size
        self.view_sudoku = view_sudoku

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            current_time = self.clock.get_ticks()
            self.view_sudoku.update(current_time)
            self._render()

            if self.view_sudoku.is_completed():
                break

            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.view_sudoku.move(dx=- self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self.view_sudoku.move(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self.view_sudoku.move(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self.view_sudoku.move(dy=self._cell_size)

                if event.key == pygame.K_1:
                    self.view_sudoku.add_number(1)
                if event.key == pygame.K_2:
                    self.view_sudoku.add_number(2)
                if event.key == pygame.K_3:
                    self.view_sudoku.add_number(3)
                if event.key == pygame.K_4:
                    self.view_sudoku.add_number(4)
                if event.key == pygame.K_5:
                    self.view_sudoku.add_number(5)
                if event.key == pygame.K_6:
                    self.view_sudoku.add_number(6)
                if event.key == pygame.K_7:
                    self.view_sudoku.add_number(7)
                if event.key == pygame.K_8:
                    self.view_sudoku.add_number(8)
                if event.key == pygame.K_9:
                    self.view_sudoku.add_number(9)

                if event.key == pygame.K_DELETE:
                    self.view_sudoku.delete_number()

            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
