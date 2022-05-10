# Luo kaikki tarvittavat spritet

import pygame
import os

dirname = os.path.dirname(__file__)


def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )


class EmptySquare(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "pictures", "emptysquare.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class OriginalNumber(pygame.sprite.Sprite):
    def __init__(self, text, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "pictures", "original_number.png"))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("Arial", 30)
        self.text = self.font.render(text, 1, (0, 0, 0))
        self.rect.x = x
        self.rect.y = y


class SelectedSquare(pygame.sprite.Sprite):
    def __init__(self, cell_size, x=0, y=0):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.color = (255, 0, 0)
        
class HorizontalLine(pygame.sprite.Sprite):
    def __init__(self, width, cell_size, x=0, y=0):
        super().__init__()
        self.image = pygame.Surface((width * cell_size, 5))
        self.rect = self.image.get_rect()
        self.color = (0,0,0)
        self.rect.x = x
        self.rect.y = y

class VerticalLine(pygame.sprite.Sprite):
    def __init__(self, height, cell_size, x=0, y=0):
        super().__init__()
        self.image = pygame.Surface((5, height*cell_size))
        self.rect = self.image.get_rect()
        self.color = (0,0,0)
        self.rect.x = x
        self.rect.y = y

class WrongNumber(pygame.sprite.Sprite):
    pass


class NumberCreatedError(pygame.sprite.Sprite):
    pass


class AddedNumber(pygame.sprite.Sprite):
    def __init__(self, text, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "pictures", "emptysquare.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.SysFont("Arial", 30)
        self.text = self.font.render(text, 1, (0, 0, 0))


class SudokuLink(pygame.sprite.Sprite):
    def __init__(self, id, center=(0,0)):
        super().__init__()
        self.font = pygame.font.SysFont("Arial", 15)
        self.text = self.font.render(f"sudoku numero: {id}", True, (0, 0, 0))
        #self.image = pygame.Surface((100, 20))
        self.rect = self.text.get_rect()
        self.rect.center = center
        self.id = id

class EnterTextField(pygame.sprite.Sprite):
    def __init__(self, text=None, x=0, y=0):
        super().__init__()
        self.font = pygame.font.SysFont("Arial", 15)
        self.text = self.font.render(text, 1, (0, 0, 0))
        self.image = pygame.Surface((200, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Button(pygame.sprite.Sprite):
    def __init__(self, text, x=0, y=0):
        super().__init__()
        self.font = pygame.font.SysFont("Arial", 15)
        self.text = self.font.render(text, 1, (0, 0, 0))
        self.image = pygame.Surface((100, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y