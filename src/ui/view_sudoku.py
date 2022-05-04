
import pygame
import os
from services.sudoku_service import sudoku_service
from entities.sudoku import OriginalSudoku, Sudoku
import ui.sprites


class ViewSudoku:
    """Sudokun näyttämisestä vastaava näkymä
    """

    def __init__(self, original_sudoku_id):
        """Luokan konstruktori, joka luo uuden Sudoku -olion.

        Args:
            original_sudoku_id: Käyttäjän käyttöliittymässä klikkaaman
            sudokun id, jonka avulla haetaan sudokuun liitetyt alkuperäiset
            numerot ja käyttäjän mahdollisesti aiemmin luoma ratkaisu.
        """
        pygame.font.init()

        self.original_sudoku = sudoku_service.find_original_numbers(
            original_sudoku_id)
        self.user_sudoku = sudoku_service.find_added_numbers(
            original_sudoku_id)
        if self.user_sudoku.user == None:
            self.user_sudoku.user = sudoku_service._user.username
        self.sprites = ui.sprites
        self.grid = self.user_sudoku.grid
        self.originals = self.original_sudoku.grid

        self.cell_size = 33
        self.empty_squares = pygame.sprite.Group()
        self.original_numbers = pygame.sprite.Group()
        self.added_numbers = pygame.sprite.Group()
        self.horizontal_lines = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.selected_square = self.sprites.SelectedSquare(self.cell_size)

        self._initialize_sprites()

    def draw_sudoku(self, display):
        """Piirtää ne osat nykyisestä sudokusta näytölle, jotka vaativat tekstin tmv.
        piirtämistä näytölle eli joiden piirtäminen ei onnistu all_sprites.draw(display) -käskyllä.

        Args:
            display: Näyttö, jolle piirretään
        """
        self.draw_added_numbers(display)
        #self.draw_lines(display)
        self.draw_original_numbers(display)
        self.draw_selected_square()

    def draw_original_numbers(self, display):
        """Piirtää näytölle sudokuun liitetyt alkuperäiset numerot.

        Args:
            display: Näyttö, jolle piirretään.
        """
        for sprite in self.original_numbers:
            display.blit(
                sprite.text, (sprite.rect.x + self.cell_size / 4, sprite.rect.y))

    def draw_added_numbers(self, display):
        """Piirtää näytölle käyttäjän lisäämät numerot.

        Args:
            display: Näyttö, jolle piirretään.
        """
        for sprite in self.added_numbers:
            display.blit(sprite.text, (sprite.rect.x +
                         self.cell_size / 4, sprite.rect.y))

    def draw_lines(self, display):
        """Piirtää näytölle sudokun 3x3 ruudukot rajaavat viivat.

        Args:
            display: Näyttö, jolle piirretään.
        """
        for i in range(len(self.grid) + 1):
            if i % 3 == 0:
                pygame.draw.line(display, (0, 0, 0), (0, i*self.cell_size),
                                 (len(self.grid) * self.cell_size, i * self.cell_size), 6)
                pygame.draw.line(display, (0, 0, 0), (i * self.cell_size, 0),
                                 (i * self.cell_size, len(self.grid) * self.cell_size), 6)

    def draw_selected_square(self):
        """Piirtää näytölle neliön, joka näyttää nykyisen valitun ruudun."""
        pygame.draw.rect(self.selected_square.image,
                         self.selected_square.color, self.selected_square.rect, 7)

    def _initialize_sprites(self):
        """Alustaa Sprite -oliot."""
        height = len(self.grid)
        width = len(self.grid[0])
        for y in range(height + 1):
            for x in range(width + 1):
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size
                if y % 3 == 0:
                    self.horizontal_lines.add(self.sprites.HorizontalLine(
                    width=width, cell_size=self.cell_size, x = 0, y = normalized_y))
                if x % 3 == 0:
                    self.horizontal_lines.add(self.sprites.VerticalLine(
                    height=height, cell_size=self.cell_size, x = normalized_x, y = 0))
                if y == height or x == height:
                    continue
                original = self.originals[y][x]
                added = self.grid[y][x]
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
                             self.original_numbers, self.selected_square, self.horizontal_lines)

    def move(self, dx=0, dy=0):
        """Muuttaa nykyisen valitun ruudun Sprite -olion x- ja y -koordinaatteja. 

        Args:
            dx: Käyttäjän nuolinäppäimillä antama x -koordinaatin suunta, johon ruutua liikutetaan.
            dy: Käyttäjän nuolinäppäimillä antama y -koordinaatin suunta, johon ruutua liikutetaan.
        """
        if self.can_move(dx, dy):
            self.selected_square.rect.move_ip(dx, dy)

    def can_move(self, dx, dy):
        """Tarkistaa, onko valittu liikkumissuunta mahdollinen.

        Args:
            dx: Käyttäjän nuolinäppäimillä antama x -koordinaatin suunta, johon ruutua liikutetaan.
            dy: Käyttäjän nuolinäppäimillä antama y -koordinaatin suunta, johon ruutua liikutetaan.

        Returns:
            Totuusarvon, joka kertoo, onko liikuttaminen mahdollista.
        """
        if (self.selected_square.rect[0] + dx < 0 or
            self.selected_square.rect[1] + dy < 0 or
            self.selected_square.rect[0] + dx + self.cell_size > 9 * self.cell_size or
                self.selected_square.rect[1] + dy + self.cell_size > 9 * self.cell_size):
            return False
        return True

    def get_coordinates(self):
        """Palauttaa nykyisen valitun ruudun koordinaatit pikseleinä.

        Returns:
            Nykyisen valitun ruudun koordinaatit pikseleinä.
        """
        return self.selected_square.rect.x, self.selected_square.rect.y

    def get_normalized_coordinates(self):
        """Palauttaa nykyisen valitun ruudun koordinaatit ruudukkoon normalisoituina.

        Returns:
            Nykyisen valitun ruudun koordinaatit normalisoituina eli valittu sijainti sudokun
            ruudukossa.
        """
        coordinates = self.get_coordinates()
        return int(coordinates[0] / self.cell_size), int(coordinates[1] / self.cell_size)

    def get_grid(self, index):
        """Etsii tiedon siitä, mihin kolmannekseen valittu indeksi kuuluu ruudukossa.

        Args:
            index: valitun ruudun rivi tai sarake

        Returns:
            Valitun ruudun kolmanneksen minimi- ja maksimiarvo.
        """
        grids = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for grid in grids:
            if index in grid:
                return min(grid), max(grid)

    def is_completed(self):
        """Tarkistaa, onko käyttäjä lisännyt kaikki numerot.
        """
        pass

    def collide_added_numbers(self):
        """Tarkistaa, minkä käyttäjän lisäämien numerojen kanssa nykyinen valittu ruutu törmää.

        Returns:
            Sprite -olion, jonka kanssa nykyinen ruutu törmää.
        """
        return pygame.sprite.spritecollide(self.selected_square, self.added_numbers, False)

    def collide_empty_squares(self):
        """Tarkistaa, minkä tyhjän ruudun kanssa nykyinen valittu ruutu törmää.

        Returns:
            Sprite -olion, jonka kanssa nykyinen ruutu törmää.
        """
        return pygame.sprite.spritecollide(self.selected_square, self.empty_squares, False)

    def add_number(self, number):
        """Muokkaa Sprite -olioita niin että lisätyn numeron ruutu on AddedNumber -luokan
        Sprite -olio, eikä EmptySquare -luokan olio, jos ruutuun saa lisätä uuden numeron.

        Args:
            number: Käyttäjän lisäämä numero, joka annetaan parametrina AddedNumber -luokalle.
        """
        column, row = self.get_normalized_coordinates()
        if sudoku_service.add_number(self.originals, self.user_sudoku, row, column, number):
            x, y = self.get_coordinates()

            for sprite in self.collide_empty_squares():
                sprite.kill()
            self.added_numbers.add(self.sprites.AddedNumber(str(number), x, y))
            self.all_sprites.add(self.added_numbers)

            sudoku_service.add_number(row=row, column=column, number=number,
                                      originals=self.original_numbers, sudoku=self.user_sudoku)

    def delete_number(self):
        """Muokkaa Sprite -olioita niin, että nykyinen ruutu on EmptySquare -luokan olio eikä
        AddedNumber -luokan olio, jos numeron poistaminen ruudusta on salittua.
        """
        column, row = self.get_normalized_coordinates()
        if sudoku_service.delete_number(self.originals, self.user_sudoku, row, column):
            for sprite in self.collide_added_numbers():
                sprite.kill()
            x, y = self.get_coordinates()
            column, row = self.get_normalized_coordinates()
            self.empty_squares.add(self.sprites.EmptySquare(x, y))
            self.all_sprites.add(self.sprites.EmptySquare(x, y))

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
