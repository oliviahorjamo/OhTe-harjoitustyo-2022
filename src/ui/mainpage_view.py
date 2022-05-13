
import pygame
from services.sudoku_service import sudoku_service
from ui import sprites


class MainpageView:
    """Pelin etusivun generoimisesta vastaava luokka
    """
    def __init__(self, display):
        pygame.font.init()
        self._display = display
        self._sprites = sprites
        self._display_height = self._display.get_height()
        self._display_width = self._display.get_width()
        self.sudokus = sudoku_service.find_all_sudokus()
        self.sudoku_links = pygame.sprite.Group()
        self.underline_sudoku = None
        self.mouse_over_logout = False
        self.initialize_sprites()

    def draw(self):
        self._display.fill((255, 255, 255))
        self.draw_text()
        self.draw_sudoku_list()
        self.draw_logout_button()

    def draw_logout_button(self):
        if self.mouse_over_logout:
            pygame.draw.rect(self._display, (206, 243, 245), self.logout_button)
        pygame.draw.rect(self._display, (0,0,0), self.logout_button, 2)
        self._display.blit(self.logout_button.text,
                          (self.logout_button.rect.x + 10, self.logout_button.rect.y))

    def draw_text(self):
        font = pygame.font.SysFont("Arial", 20)
        description = font.render(
            "Valitse sudoku, jota haluat pelata", True, (0, 0, 0))
        description_rect = description.get_rect()
        description_rect.center = (self._display_width // 2, 45)
        self._display.blit(description, description_rect)

    def draw_sudoku_list(self):
        for sprite in self.sudoku_links:
            if sprite.id == self.underline_sudoku:
                pygame.draw.line(self._display, (0,0,0), (sprite.rect.x, sprite.rect.y + sprite.rect.height), 
                                (sprite.rect.x + sprite.rect.width, sprite.rect.y + sprite.rect.height))
            self._display.blit(
                sprite.text, sprite.rect)

    def initialize_sprites(self):
        i = 0
        for sudoku in self.sudokus:
            i += 1
            self.sudoku_links.add(self._sprites.SudokuLink(
                sudoku.id, center = (self._display_width // 2, self._display_height / 4 + 20*i)))
        
        self.logout_button = self._sprites.Button("Log out", x = 400, y = 20)

    def select_sudoku(self, mouse):
        for sudoku in self.sudoku_links:
            if sudoku.rect.collidepoint(mouse):
                return sudoku.id

    def logout_button_collide(self, mouse):
        if self.logout_button.rect.collidepoint(mouse):
            return True


#mainpage = Mainpage()
