
import pygame
from services.sudoku_service import sudoku_service
from ui import sprites
from ui.general_ui import GeneralUIDrawing


class MainpageView:
    """Pelin etusivun generoimisesta vastaava luokka
    """

    def __init__(self, display):
        """Luokan konstruktori, joka luo uuden MainpageView -luokan olion.

        Args:
            display: Näyttö, jolle luokan piirtofunktiot piirtävät.
        """
        pygame.font.init()
        self._display = display
        self._display_height = self._display.get_height()
        self._display_width = self._display.get_width()
        self._sudokus = sudoku_service.find_all_sudokus()
        self.underlined_sudoku = None
        self.mouse_over_logout_button = False
        self._general_ui = GeneralUIDrawing(self._display)
        self._sprites = sprites
        self._sudoku_links = pygame.sprite.Group()
        self.initialize_sprites()

    def draw(self):
        """Piirtää etusivun näkymän
        """
        self._display.fill((255, 255, 255))
        self.draw_text()
        self.draw_sudoku_list()
        self.draw_logout_button()

    def draw_logout_button(self):
        """Kutsuu uloskirjautmis -painikkeen piirtävää funktiota
        """
        self._general_ui.draw_button(button=self._logout_button,
                                     mouse_over_button=self.mouse_over_logout_button)

    def draw_text(self):
        """Piirtää näytölle ohjetekstin
        """
        font = pygame.font.SysFont("Arial", 20)
        description = font.render(
            "Valitse sudoku, jota haluat pelata", True, (0, 0, 0))
        description_rect = description.get_rect()
        description_rect.center = (self._display_width // 2, 45)
        self._display.blit(description, description_rect)

    def draw_sudoku_list(self):
        """Piirtää näytölle kaikki sudokulinkit
        """
        for sprite in self._sudoku_links:
            if sprite.id == self.underlined_sudoku:
                pygame.draw.line(self._display, (0, 0, 0), (sprite.rect.x, sprite.rect.y + sprite.rect.height),
                                 (sprite.rect.x + sprite.rect.width, sprite.rect.y + sprite.rect.height))
            self._display.blit(
                sprite.text, sprite.rect)

    def initialize_sprites(self):
        """Alustaa näkymään liittyvät Sprite -oliot
        """
        i = 0
        for sudoku in self._sudokus:
            i += 1
            self._sudoku_links.add(self._sprites.SudokuLink(
                sudoku.id, center=(self._display_width // 2, self._display_height / 4 + 20*i)))
        self._logout_button = self._sprites.Button("Log out", x=400, y=20)

    def select_sudoku(self, mouse):
        """Kertoo, onko jotakin sudokulinkkiä klikattu listassa

        Args:
            mouse: käyttäjän hiiren koordinaatit klikkauksen hetkellä

        Returns:
            Klikatun sudokun alkuperäisiin numeroihin liitetyn id -numeron,
            jos jotain sudokulinkkiä on klikattu.
        """
        for sudoku in self._sudoku_links:
            if sudoku.rect.collidepoint(mouse):
                return sudoku.id

    def logout_button_collide(self, mouse):
        """Kertoo, onko uloskirjautumis -painiketta painettu.

        Args:
            mouse: käyttäjän hiiren koordinaatit klikkauksen hetkellä

        Returns:
            true, jos käyttäjä on klikannut uloskirjautumis -painiketta.
        """
        if self._logout_button.rect.collidepoint(mouse):
            return True
