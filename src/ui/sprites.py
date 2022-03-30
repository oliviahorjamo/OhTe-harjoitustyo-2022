#Luo kaikki tarvittavat spritet

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
        self.image = pygame.image.load(os.path.join(dirname, "pictures", "emptysquare.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class OriginalNumber(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(os.path.join(dirname, "pictures", "original_number.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class SelectedSquare(pygame.sprite.Sprite):
    pass

class WrongNumber(pygame.sprite.Sprite):
    pass

class NumberCreatedError(pygame.sprite.Sprite):
    pass

class AddedNumber(pygame.sprite.Sprite):
    pass
