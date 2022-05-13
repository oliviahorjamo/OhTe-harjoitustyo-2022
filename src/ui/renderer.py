import pygame

class Renderer:
    def __init__(self, current_view=None):
        self.current_view = current_view

    def render(self):
        self.current_view.draw()
        pygame.display.update()
