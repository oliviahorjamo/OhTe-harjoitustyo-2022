
import pygame
import os
from services.sudoku_service import sudoku_service
from entities.sudoku import OriginalSudoku, Sudoku
import ui.sprites


class ViewSudoku:

    def __init__(self, id):

        pygame.font.init()

        original_sudoku = sudoku_service.find_original_numbers(id)
        user_sudoku = sudoku_service.find_added_numbers(id)
        if user_sudoku.user == None:
            user_sudoku.user = sudoku_service._user.username
        print("user sudoku name", user_sudoku.user)
        self.sprites = ui.sprites
        self.grid = user_sudoku.grid
        self.originals = original_sudoku.grid
        self.user_sudoku = user_sudoku
        self.cell_size = 33
        self.display = pygame.display.set_mode((500, 500))
        self.empty_squares = pygame.sprite.Group()
        self.original_numbers = pygame.sprite.Group()
        self.added_numbers = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.selected_square = self.sprites.SelectedSquare(self.cell_size)

        self._initialize_sprites(self.grid, self.originals)

    def draw_sudoku(self, display):
        self.draw_added_numbers(display)
        self.draw_lines(display)
        self.draw_original_numbers(display)
        self.draw_selected_square()

    def draw_original_numbers(self, display):
        for sprite in self.original_numbers:
            display.blit(
                sprite.text, (sprite.rect.x + self.cell_size / 4, sprite.rect.y))

    def draw_added_numbers(self, display):
        for sprite in self.added_numbers:
            display.blit(sprite.text, (sprite.rect.x +
                         self.cell_size / 4, sprite.rect.y))

    def draw_lines(self, display):
        for i in range(len(self.grid) + 1):
            if i % 3 == 0:
                pygame.draw.line(display, (0, 0, 0), (0, i*self.cell_size),
                                 (len(self.grid) * self.cell_size, i * self.cell_size), 6)
                pygame.draw.line(display, (0, 0, 0), (i * self.cell_size, 0),
                                 (i * self.cell_size, len(self.grid) * self.cell_size), 6)

    def draw_selected_square(self):
        pygame.draw.rect(self.selected_square.image,
                         self.selected_square.color, self.selected_square.rect, 7)

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
        if sudoku_service.add_number(self.originals, self.user_sudoku, row, column, number):
            x, y = self.get_coordinates()

            for sprite in self.collide_empty_squares():
                sprite.kill()
            self.added_numbers.add(self.sprites.AddedNumber(str(number), x, y))
            self.all_sprites.add(self.added_numbers)

            sudoku_service.add_number(row = row, column = column, number = number, originals=self.original_numbers, sudoku = self.user_sudoku)

            #self.check_column(row=row, column=column, number=number)
            #self.check_row(column=column, row=row, number=number)
            #self.check_small_grid(row=row, column=column, number=number)

    def delete_number(self):
        column, row = self.get_normalized_coordinates()
        if sudoku_service.delete_number(self.originals, self.user_sudoku, row, column):
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
