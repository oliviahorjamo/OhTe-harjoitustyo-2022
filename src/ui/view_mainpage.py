
import pygame
from services.sudoku_service import sudoku_service
from ui import sprites
from ui.view_login import login_view


class Mainpage:
    """Pelin etusivun generoimisesta vastaava luokka
    """
    def __init__(self):
        pygame.font.init()
        self.sprites = sprites
        self.display_height = login_view.display.get_height()
        self.display_width = login_view.display.get_width()
        self.sudokus = sudoku_service.find_all_sudokus()
        self.sudoku_links = pygame.sprite.Group()
        self.underline_sudoku = None
        self.mouse_over_logout = False
        self.initialize_sprites()

    def draw_mainpage(self, display):
        self.draw_text(display)
        self.draw_sudoku_list(display)
        self.draw_logout_button(display)

    def draw_logout_button(self, display):
        if self.mouse_over_logout:
            pygame.draw.rect(display, (206, 243, 245), self.logout_button)
        pygame.draw.rect(display, (0,0,0), self.logout_button, 2)
        display.blit(self.logout_button.text,
                          (self.logout_button.rect.x + 10, self.logout_button.rect.y))

    def draw_text(self, display):
        font = pygame.font.SysFont("Arial", 20)
        description = font.render(
            "Valitse sudoku, jota haluat pelata", True, (0, 0, 0))
        description_rect = description.get_rect()
        description_rect.center = (self.display_width // 2, 45)
        display.blit(description, description_rect)

    def draw_sudoku_list(self, display):
        for sprite in self.sudoku_links:
            if sprite.id == self.underline_sudoku:
                pygame.draw.line(display, (0,0,0), (sprite.rect.x, sprite.rect.y + sprite.rect.height), 
                                (sprite.rect.x + sprite.rect.width, sprite.rect.y + sprite.rect.height))
            display.blit(
                sprite.text, sprite.rect)

    def initialize_sprites(self):
        i = 0
        for sudoku in self.sudokus:
            i += 1
            self.sudoku_links.add(self.sprites.SudokuLink(
                sudoku.id, center = (self.display_width // 2, self.display_height / 4 + 20*i)))
        
        self.logout_button = self.sprites.Button("Log out", x = 400, y = 20)

    def select_sudoku(self, mouse):
        for sudoku in self.sudoku_links:
            if sudoku.rect.collidepoint(mouse):
                return sudoku.id

    def logout_button_collide(self, mouse):
        if self.logout_button.rect.collidepoint(mouse):
            return True


mainpage = Mainpage()
