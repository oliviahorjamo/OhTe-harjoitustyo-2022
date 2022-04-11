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
        #pygame.draw.rect(self.image, self.color, self.rect, 7)


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
