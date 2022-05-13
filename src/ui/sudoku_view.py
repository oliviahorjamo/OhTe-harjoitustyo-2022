
import pygame
from services.sudoku_service import sudoku_service
from ui.general_ui import GeneralUIDrawing
import ui.sprites


class SudokuView:
    """Sudokun näyttämisestä vastaava näkymä
    """

    def __init__(self, original_sudoku_id, display):
        """Luokan konstruktori, joka luo uuden Sudoku -olion.

        Args:
            original_sudoku_id: Käyttäjän käyttöliittymässä klikkaaman
            sudokun id, jonka avulla haetaan sudokuun liitetyt alkuperäiset
            numerot ja käyttäjän mahdollisesti aiemmin luoma ratkaisu.
        """
        pygame.font.init()
        self._general_ui = GeneralUIDrawing(display)
        self._display = display
        self._original_sudoku = sudoku_service.find_original_numbers(
            original_sudoku_id)
        self._user_sudoku = sudoku_service.find_added_numbers(
            original_sudoku_id)
        self._user_sudoku_grid = self._user_sudoku.grid
        self._original_sudoku_grid = self._original_sudoku.grid

        self.mouse_over_logout_button = False
        self.mouse_over_return_button = False

        self.cell_size = 33
        self._sprites = ui.sprites
        self._empty_squares = pygame.sprite.Group()
        self._original_numbers = pygame.sprite.Group()
        self._added_numbers = pygame.sprite.Group()
        self._lines = pygame.sprite.Group()
        self._all_sprites = pygame.sprite.Group()

        self._initialize_sprites()

    def _initialize_sprites(self):
        """Alustaa Sprite -oliot."""
        self._initialize_individual_sprites()
        height = len(self._user_sudoku_grid)
        width = len(self._user_sudoku_grid[0])
        for y in range(height + 1):
            for x in range(width + 1):
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size
                if y % 3 == 0:
                    self._lines.add(self._sprites.HorizontalLine(
                    width=width, cell_size=self.cell_size, x = 0, y = normalized_y))
                if x % 3 == 0:
                    self._lines.add(self._sprites.VerticalLine(
                    height=height, cell_size=self.cell_size, x = normalized_x, y = 0))
                if y == height or x == height:
                    continue
                original = self._original_sudoku_grid[y][x]
                added = self._user_sudoku_grid[y][x]
                if added == 0 and original == 0:
                    self._empty_squares.add(
                        self._sprites.EmptySquare(normalized_x, normalized_y))
                elif original != 0:
                    self._original_numbers.add(self._sprites.OriginalNumber(
                        str(original), normalized_x, normalized_y))
                elif added != 0:
                    self._added_numbers.add(self._sprites.AddedNumber(
                        str(added), normalized_x, normalized_y))
        self._all_sprites.add(self._empty_squares,
                             self._original_numbers, self._selected_square, self._lines)

    def _initialize_individual_sprites(self):
        self._selected_square = self._sprites.SelectedSquare(self.cell_size)
        self._logout_button = self._sprites.Button("Log out", x=400, y = 20)
        self._return_button = self._sprites.Button("Return", x = 400, y = 45)


    def draw(self):
        """Piirtää pelinäkymän näytölle.

        Args:
            display: Näyttö, jolle piirretään
        """
        self._display.fill((255, 255, 255))
        self._all_sprites.draw(self._display)
        self._lines.draw(self._display)
        self.draw_added_numbers()
        self.draw_original_numbers()
        self.draw_selected_square()
        self.draw_buttons()

    def draw_buttons(self):
        """Kutsuu painikkeita piirtävää funktiota.
        """
        self._general_ui.draw_button(button=self._logout_button,
            mouse_over_button=self.mouse_over_logout_button)
        self._general_ui.draw_button(button=self._return_button,
            mouse_over_button=self.mouse_over_return_button)

    def draw_original_numbers(self):
        """Piirtää näytölle sudokuun liitetyt alkuperäiset numerot.

        Args:
            display: Näyttö, jolle piirretään.
        """
        for sprite in self._original_numbers:
            self._display.blit(
                sprite.text, (sprite.rect.x + self.cell_size / 4, sprite.rect.y))

    def draw_added_numbers(self):
        """Piirtää näytölle käyttäjän lisäämät numerot.

        Args:
            display: Näyttö, jolle piirretään.
        """
        for sprite in self._added_numbers:
            self._display.blit(sprite.text, (sprite.rect.x +
                         self.cell_size / 4, sprite.rect.y))


    def draw_selected_square(self):
        """Piirtää näytölle neliön, joka näyttää nykyisen valitun ruudun."""
        pygame.draw.rect(self._selected_square.image,
                         self._selected_square.color, self._selected_square.rect, 3)

    def add_selected_square_to_top(self):
        """Lisää valintaruudun Sprite -olion kaikki spritet sisältävän
        joukon viimeiseksi, jotta se piirretään viimeisenä, eikä peity
        myöhemmin lisätyillä Sprite -olioilla.
        """
        selected_square_old = self._selected_square
        self._selected_square.kill()
        self._selected_square = selected_square_old
        self._all_sprites.add(selected_square_old)

    def move(self, dx=0, dy=0):
        """Muuttaa nykyisen valitun ruudun Sprite -olion x- ja y -koordinaatteja. 

        Args:
            dx: Käyttäjän nuolinäppäimillä antama x -koordinaatin suunta, johon ruutua liikutetaan.
            dy: Käyttäjän nuolinäppäimillä antama y -koordinaatin suunta, johon ruutua liikutetaan.
        """
        if self.can_move(dx, dy):
            self._selected_square.rect.move_ip(dx, dy)

    def can_move(self, dx, dy):
        """Tarkistaa, onko valittu liikkumissuunta mahdollinen.

        Args:
            dx: Käyttäjän nuolinäppäimillä antama x -koordinaatin suunta, johon ruutua liikutetaan.
            dy: Käyttäjän nuolinäppäimillä antama y -koordinaatin suunta, johon ruutua liikutetaan.

        Returns:
            Totuusarvon, joka kertoo, onko liikuttaminen mahdollista.
        """
        if (self._selected_square.rect[0] + dx < 0 or
            self._selected_square.rect[1] + dy < 0 or
            self._selected_square.rect[0] + dx + self.cell_size > 9 * self.cell_size or
                self._selected_square.rect[1] + dy + self.cell_size > 9 * self.cell_size):
            return False
        return True

    def get_coordinates(self):
        """Palauttaa nykyisen valitun ruudun koordinaatit pikseleinä.

        Returns:
            Nykyisen valitun ruudun koordinaatit pikseleinä.
        """
        return self._selected_square.rect.x, self._selected_square.rect.y

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

    def collide_added_numbers(self):
        """Tarkistaa, minkä käyttäjän lisäämien numerojen kanssa nykyinen valittu ruutu törmää.

        Returns:
            Sprite -olion, jonka kanssa nykyinen ruutu törmää.
        """
        return pygame.sprite.spritecollide(self._selected_square, self._added_numbers, False)

    def collide_empty_squares(self):
        """Tarkistaa, minkä tyhjän ruudun kanssa nykyinen valittu ruutu törmää.

        Returns:
            Sprite -olion, jonka kanssa nykyinen ruutu törmää.
        """
        return pygame.sprite.spritecollide(self._selected_square, self._empty_squares, False)

    def add_number(self, number):
        """Muokkaa Sprite -olioita niin että lisätyn numeron ruutu on AddedNumber -luokan
        Sprite -olio, eikä EmptySquare -luokan olio, jos ruutuun saa lisätä uuden numeron.

        Args:
            number: Käyttäjän lisäämä numero, joka annetaan parametrina AddedNumber -luokalle.
        """
        column, row = self.get_normalized_coordinates()
        if sudoku_service.add_number(self._original_sudoku_grid, self._user_sudoku, row, column, number):
            x, y = self.get_coordinates()

            for sprite in self.collide_empty_squares():
                sprite.kill()
            for sprite in self.collide_added_numbers():
                sprite.kill()
            self._added_numbers.add(self._sprites.AddedNumber(str(number), x, y))
            self._all_sprites.add(self._added_numbers)
        self.add_selected_square_to_top()

    def delete_number(self):
        """Muokkaa Sprite -olioita niin, että nykyinen ruutu on EmptySquare -luokan olio eikä
        AddedNumber -luokan olio, jos numeron poistaminen ruudusta on salittua.
        """
        column, row = self.get_normalized_coordinates()
        if sudoku_service.delete_number(self._original_sudoku_grid, self._user_sudoku, row, column):
            for sprite in self.collide_added_numbers():
                sprite.kill()
            x, y = self.get_coordinates()
            column, row = self.get_normalized_coordinates()
            self._empty_squares.add(self._sprites.EmptySquare(x, y))
            self._all_sprites.add(self._sprites.EmptySquare(x, y))
        self.add_selected_square_to_top()

    def logout_button_collide(self, mouse):
        if self._logout_button.rect.collidepoint(mouse):
            return True

    def back_button_collide(self, mouse):
        if self._return_button.rect.collidepoint(mouse):
            return True