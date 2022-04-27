
# Tämä tiedosto käsittelee sisään kirjautumiseen ja uuden käyttäjän luomiseen littyvän käyttöliittymän
import pygame

from ui.sprites import EnterTextField, Button


class LoginView:
    def __init__(self):
        pygame.font.init()
        display_height = 500
        display_width = 500
        self.display = pygame.display.set_mode((display_width, display_height))
        self.username = ""
        self.password = ""
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites()

    def _initialize_sprites(self):
        self.username_field = EnterTextField(
            x=self.display.get_width() / 4, y=50)
        self.password_field = EnterTextField(
            x=self.display.get_width() / 4, y=100)
        self.login_button = Button(
            text="Log in", x=self.display.get_width() / 4, y=150)
        self.create_user_button = Button(
            text="Create user", x=self.display.get_width() / 4, y=200)
        self.all_sprites.add(self.username_field, self.password_field, self.login_button, self.create_user_button)

    def draw_login_view(self):
        self.draw_login_fields()
        self.draw_login_button()
        self.draw_create_user_button

    def draw_login_fields(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.username_field.rect, 3)
        pygame.draw.rect(self.display, (0, 0, 0), self.password_field.rect, 3)
        self.username_text = self.username_field.font.render(
            "Käyttäjänimi", 1, (0, 0, 0))
        self.display.blit(
            self.username_text, (self.username_field.rect.x, self.username_field.rect.y - 30))
        self.password_text = self.password_field.font.render(
            "Salasana", 1, (0, 0, 0))
        self.display.blit(
            self.password_text, (self.password_field.rect.x + 10, self.password_field.rect.y - 30))
        text = self.username_field.font.render(self.username, 1, (0, 0, 0))
        self.display.blit(
            text, (self.username_field.rect.x + 10, self.username_field.rect.y))
        text = self.password_field.font.render(self.password, 1, (0, 0, 0))
        self.display.blit(
            text, (self.password_field.rect.x + 10, self.password_field.rect.y))

    def draw_login_button(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.login_button, 2)
        self.display.blit(self.login_button.text,
                          (self.login_button.rect.x + 10, self.login_button.rect.y))

    def draw_create_user_button(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.create_user_button, 2)
        self.display.blit(self.create_user_button.text,
                          (self.create_user_button.rect.x + 10, self.create_user_button.rect.y))

    def username_field_collide(self, mouse):
        if self.username_field.rect.collidepoint(mouse):
            return True

    def password_field_collide(self, mouse):
        if self.password_field.rect.collidepoint(mouse):
            return True

    def login_button_collide(self, mouse):
        if self.login_button.rect.collidepoint(mouse):
            return True

    def create_user_button_collide(self, mouse):
        if self.create_user_button.rect.collidepoint(mouse):
            return True


login_view = LoginView()
