
import pygame
from services.sudoku_service import sudoku_service
from ui import sprites
from ui.view_login import login_view


class Mainpage:
    """Pelin etusivun generoimisesta vastaava luokka
    """
    def __init__(self):
        pygame.font.init()
        self.display_height = login_view.display.get_height()
        self.display_width = login_view.display.get_width()
        self.sudokus = sudoku_service.find_all_sudokus()
        self.sudoku_links = pygame.sprite.Group()
        self.underline_sudoku = None
        self.initialize_sprites()

    def draw_mainpage(self, display):
        self.draw_text(display)
        self.draw_sudoku_list(display)

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
            self.sudoku_links.add(sprites.SudokuLink(
                sudoku.id, center = (self.display_width // 2, self.display_height / 4 + 20*i)))

    def select_sudoku(self, mouse):
        for sudoku in self.sudoku_links:
            if sudoku.rect.collidepoint(mouse):
                return sudoku.id

class SudokuList:
    def __init__(self):
        pass


mainpage = Mainpage()
