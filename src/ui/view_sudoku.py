
import pygame
import os
from services.sudoku_service import sudoku_service
from entities.sudoku import OriginalSudoku


class ViewSudoku:

    def __init__(self, cell_size, sprites, sudoku, original):

        pygame.font.init()

        self.sprites = sprites
        self.grid = sudoku.grid
        self.originals = original.grid
        self.sudoku = sudoku
        self.cell_size = cell_size

        self.empty_squares = pygame.sprite.Group()
        self.original_numbers = pygame.sprite.Group()
        self.selected_square = sprites.SelectedSquare(self.cell_size)
        self.added_numbers = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(self.grid, self.originals)

    def get_coordinate():
        # palauttaa hiiren kohdalla olevan koordinaatin
        pass

    def draw_lines_and_numbers():
        pass

    def draw_unvalid():
        # korostaa punaisella epävalidin vastauksen syyn
        pass

    def _initialize_sprites(self, grid, originals):
        height = len(grid)
        width = len(grid[0])
        for y in range(height):
            for x in range(width):
                original = originals[y][x]
                added = grid[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size
                if added == 0 and original == 0:
                    self.empty_squares.add(
                        self.sprites.EmptySquare(normalized_x, normalized_y))
                elif original != 0:
                    self.original_numbers.add(self.sprites.OriginalNumber(
                        str(original), normalized_x, normalized_y))
                elif added != 0:
                    self.added_numbers.add(self.sprites.AddedNumber(
                        str(added), normalized_x, normalized_y))
        self.all_sprites.add(self.empty_squares,
                             self.original_numbers, self.selected_square)

    def move(self, dx=0, dy=0):
        if self.can_move(dx, dy):
            self.selected_square.rect.move_ip(dx, dy)

    def can_move(self, dx, dy):
        if (self.selected_square.rect[0] + dx < 0 or
            self.selected_square.rect[1] + dy < 0 or
            self.selected_square.rect[0] + dx + self.cell_size > 9 * self.cell_size or
                self.selected_square.rect[1] + dy + self.cell_size > 9 * self.cell_size):
            return False
        return True

    def get_coordinates(self):
        return self.selected_square.rect.x, self.selected_square.rect.y

    def get_normalized_coordinates(self):
        coordinates = self.get_coordinates()
        return int(coordinates[0] / self.cell_size), int(coordinates[1] / self.cell_size)

    def get_grid(self, index):
        grids = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for grid in grids:
            if index in grid:
                return min(grid), max(grid)

    def update(self, current_time):
        pass

    def is_completed(self):
        pass

    def collide_original_numbers(self):
        return pygame.sprite.spritecollide(self.selected_square, self.original_numbers, False)

    def collide_added_numbers(self):
        return pygame.sprite.spritecollide(self.selected_square, self.added_numbers, False)

    def collide_empty_squares(self):
        return pygame.sprite.spritecollide(self.selected_square, self.empty_squares, False)

    def add_number(self, number):
        column, row = self.get_normalized_coordinates()
        if sudoku_service.add_number(self.originals, self.sudoku, row, column, number):
            x, y = self.get_coordinates()

            for sprite in self.collide_empty_squares():
                sprite.kill()
            self.added_numbers.add(self.sprites.AddedNumber(str(number), x, y))
            self.all_sprites.add(self.added_numbers)

            self.check_column(row=row, column=column, number=number)
            self.check_row(column=column, row=row, number=number)
            self.check_small_grid(row=row, column=column, number=number)

    def delete_number(self):
        column, row = self.get_normalized_coordinates()
        if sudoku_service.delete_number(self.originals, self.sudoku, row, column):
            # testaus ettei numero oo alkuperäinen eli voi poistaa
            for sprite in self.collide_added_numbers():
                sprite.kill()
            x, y = self.get_coordinates()
            column, row = self.get_normalized_coordinates()
            self.empty_squares.add(self.sprites.EmptySquare(x, y))
            self.all_sprites.add(self.sprites.EmptySquare(x, y))

    # näitä ei käytetä sittenkään eli ei anneta virheviestiä heti jos käyttäjä tekee virheen vaan vasta kun valmis

    def check_row(self, column, row, number):
        column_index = -1
        for value in self.grid[row]:
            column_index += 1
            if value == number and column_index != column:
                print("samalla rivillä virhe!")

    def check_column(self, row, column, number):
        for row_index in range(len(self.grid)):
            for column_index in range(len(self.grid[0])):
                if column_index == column and self.grid[row_index][column_index] == number and row_index != row:
                    print("samassa kolumnissa virhe")
                    print("row", row, "column_index", column_index,
                          "number", self.grid[row][column_index])

    def check_small_grid(self, row, column, number):
        row_min, row_max = self.get_grid(row)
        column_min, column_max = self.get_grid(column)
        for row_value in range(row_min, row_max + 1):
            for column_value in range(column_min, column_max + 1):
                if self.grid[row_value][column_value] == number and not (row_value == row and column_value == column):
                    print("samassa ruudukossa virhe")


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


class Clock:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        self.clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()


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
