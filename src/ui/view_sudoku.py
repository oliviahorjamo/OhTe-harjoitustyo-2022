
from types import CellType
import pygame
import os
#import sprites
#from entities.sudoku import Sudoku

class ViewSudoku:

    def __init__(self, cell_size, sprites, sudoku):

        pygame.font.init()

        self.sprites = sprites
        self.grid = sudoku.grid
        self.cell_size = cell_size

        self.empty_squares = pygame.sprite.Group()
        self.original_numbers = pygame.sprite.Group()
        self.selected_square = sprites.SelectedSquare(self.cell_size)
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(sudoku.grid)

    def get_coordinate():
        #palauttaa hiiren kohdalla olevan koordinaatin
        pass

    def draw_lines_and_numbers():
        pass
        
    def draw_unvalid():
        #korostaa punaisella epävalidin vastauksen syyn
        pass

    def _initialize_sprites(self, grid):
        height = len(grid)
        width = len(grid[0])
        for y in range(height):
            for x in range(width):
                cell = grid[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size
                if cell == 0:
                    self.empty_squares.add(self.sprites.EmptySquare(normalized_x, normalized_y))
                else:
                    self.original_numbers.add(self.sprites.OriginalNumber(str(cell), normalized_x, normalized_y))
        self.all_sprites.add(self.empty_squares, self.original_numbers, self.selected_square)

    def move(self, dx = 0, dy = 0):
        #tän pitäis liikuttaa valitun ruudun neliötä
        #self._level.move_robot(dx=-self._cell_size)
        
        #TODO virheen käsittely eli katsoo ettei mee ruudukosta yli
        self.selected_square.rect.move_ip(dx, dy)

    def update(self, current_time):
        pass

    def is_completed(self):
        pass

    def add_number(self, number):
        #TODO lisää testit ettei voi lisätä alkuperäsen tai vanhan numeron päälle
        coordinates = self.selected_square.rect
        column = int(coordinates[0] / self.cell_size)
        row = int(coordinates[1] / self.cell_size)
        print(row, column)
        
        print(coordinates)
        print("grid", self.grid)
        self.grid[row][column] = number
        print("grid lopuksi", self.grid)

class GameLoop:

    #pyörittää peliä eli tarkistaa mitä näppäimiä on painettu ja toimii sen mukaisesti
    #automaattisesti päivittää näyttöä

    def __init__(self, view_sudoku, cell_size, renderer):
        self._renderer = renderer
        #self._event_queue = pygame.event.get()
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

    #def draw_lines_and_numbers(self):
        #piirtää sudokun viivat ja täyttää värillä numerot jotka jo täytetty


    def _handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.view_sudoku.move(dx = - self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self.view_sudoku.move(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self.view_sudoku.move(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self.view_sudoku.move(dy=self._cell_size)

                if event.key == pygame.K_0:
                    #tässä kohtaa pitäis asettaa numero myös pelin omaan gridiin
                    #elf.view_sudoku.add_number(x, y, number)
                    self.view_sudoku.add_number(0)

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
        self.view_sudoku.all_sprites.draw(self._display)

        for sprite in self.view_sudoku.original_numbers:
            self._display.blit(sprite.text, (sprite.rect.x, sprite.rect.y))

        for i in range(len(self.view_sudoku.grid)):
            if i % 3 == 0:
                pygame.draw.line(self._display, (0,0,0), (0, i*self.view_sudoku.cell_size), (pygame.display.get_surface().get_width(), i * self.view_sudoku.cell_size), 6)
                pygame.draw.line(self._display, (0,0,0), (i * self.view_sudoku.cell_size, 0), (i * self.view_sudoku.cell_size, pygame.display.get_surface().get_height()), 6)

        pygame.display.update()