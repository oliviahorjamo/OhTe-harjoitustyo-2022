import pygame

class Renderer:
    def __init__(self, display, view_sudoku):
        self._display = display
        self.view_sudoku = view_sudoku

    def render(self):
        self._display.fill((255, 255, 255))
        self.view_sudoku.all_sprites.draw(self._display)

        for sprite in self.view_sudoku.original_numbers:
            self._display.blit(
                sprite.text, (sprite.rect.x + self.view_sudoku.cell_size / 4, sprite.rect.y))

        for sprite in self.view_sudoku.added_numbers:
            self._display.blit(sprite.text, (sprite.rect.x + self.view_sudoku.cell_size / 4, sprite.rect.y))

        for i in range(len(self.view_sudoku.grid)):
            if i % 3 == 0:
                pygame.draw.line(self._display, (0, 0, 0), (0, i*self.view_sudoku.cell_size),
                                 (pygame.display.get_surface().get_width(), i * self.view_sudoku.cell_size), 6)
                pygame.draw.line(self._display, (0, 0, 0), (i * self.view_sudoku.cell_size, 0),
                                 (i * self.view_sudoku.cell_size, pygame.display.get_surface().get_height()), 6)

        pygame.draw.rect(self.view_sudoku.selected_square.image,
                         self.view_sudoku.selected_square.color, self.view_sudoku.selected_square.rect, 7)

        pygame.display.update()
