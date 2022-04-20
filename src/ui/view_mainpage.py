
# Tämä moduuli sisältää sovelluksen käyttöliittymän etusivun koodin

import pygame
import os
from ui.renderer import Renderer

class Mainpage:
    def __init__(self):
        display_height = 500
        display_width = 500
        self.display = pygame.display.set_mode((display_width, display_height))

    def start_mainpage(self):
        pass

class SudokuList:
    def __init__(self):
        pass

mainpage = Mainpage()