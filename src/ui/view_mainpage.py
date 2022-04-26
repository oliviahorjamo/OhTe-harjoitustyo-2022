
# Tämä moduuli sisältää sovelluksen käyttöliittymän etusivun koodin

import pygame
import os
from services.sudoku_service import sudoku_service
from ui import sprites


class Mainpage:
    def __init__(self):
        pygame.font.init()
        display_height = 500
        display_width = 500
        self.display = pygame.display.set_mode((display_width, display_height))
        self.sudokus = sudoku_service.find_all_sudokus()
        self.sudoku_links = pygame.sprite.Group()
        self.initialize_sprites()

    def draw_text(self, display):
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("SUDOKU MAINPAGE", False, (0, 0, 0))
        display.blit(text, (20, 20))
        text = font.render(
            "Valitse sudoku, jota haluat pelata", False, (0, 0, 0))
        display.blit(text, (20, 45))

    def draw_sudoku_list(self, display):
        for sprite in self.sudoku_links:
            display.blit(
                sprite.text, (sprite.rect.x, sprite.rect.y))

    def initialize_sprites(self):
        i = 0
        for sudoku in self.sudokus:
            i += 1
            self.sudoku_links.add(sprites.SudokuLink(
                sudoku.id, self.display.get_width() / 4, self.display.get_height() / 4 + 20*i))

    def select_sudoku(self, mouse):
        for sudoku in self.sudoku_links:
            if sudoku.rect.collidepoint(mouse):
                return sudoku.id


class SudokuList:
    def __init__(self):
        pass


mainpage = Mainpage()
