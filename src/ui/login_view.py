
# Tämä tiedosto käsittelee sisään kirjautumiseen ja uuden käyttäjän luomiseen littyvän käyttöliittymän
import pygame
from ui.sprites import EnterTextField, Button, Error


class LoginView:
    def __init__(self, display):
        pygame.font.init()
        self.error_happened = False
        self._display = display
        self.username = ""
        self.password = ""
        self.all_sprites = pygame.sprite.Group()
        self.username_field_clicked = False
        self.password_field_clicked = False
        self.mouse_over_login_button = False
        self.mouse_over_create_user_button = False
        self._initialize_sprites()

    def _initialize_sprites(self):
        self.username_field = EnterTextField(
            x=self._display.get_width() / 4, y=50)
        self.password_field = EnterTextField(
            x=self._display.get_width() / 4, y=100)
        self.login_button = Button(
            text="Log in", x=self._display.get_width() / 4, y=150)
        self.create_user_button = Button(
            text="Create user", x=self._display.get_width() / 4, y=200)
        self.all_sprites.add(self.username_field, self.password_field,
                             self.login_button, self.create_user_button)

    def draw(self):
        self._display.fill((255, 255, 255))
        self.draw_login_fields()
        self.draw_login_button()
        self.draw_create_user_button()
        if self.error_happened:
            self.draw_error_message()

    def draw_error_message(self):
        self._display.blit(self.error_message.text, self.error_message.rect)


    def draw_login_fields(self):
        self.draw_username_field()
        self.draw_password_field()

    def draw_username_field(self):
        if self.username_field_clicked:
            pygame.draw.rect(self._display, (206, 243, 245), self.username_field.rect)
        pygame.draw.rect(self._display, (0, 0, 0), self.username_field.rect, 2)
        description = self.username_field.font.render(
            "Käyttäjänimi", 1, (0, 0, 0))
        self._display.blit(
            description, (self.username_field.rect.x, self.username_field.rect.y - 30))
        text_surface = self.username_field.font.render(self.username, 1, (0, 0, 0))
        self._display.blit(
            text_surface, (self.username_field.rect.x + 10, self.username_field.rect.y))

    def draw_password_field(self):
        if self.password_field_clicked:
            pygame.draw.rect(self._display, (206, 243, 245), self.password_field.rect)
        pygame.draw.rect(self._display, (0, 0, 0), self.password_field.rect, 2)
        self.password_text = self.password_field.font.render(
            "Salasana", 1, (0, 0, 0))
        self._display.blit(
            self.password_text, (self.password_field.rect.x + 10, self.password_field.rect.y - 30))
        password_text = self.password_field.font.render(self.password, 1, (0, 0, 0))
        self._display.blit(
            password_text, (self.password_field.rect.x + 10, self.password_field.rect.y))

    def draw_login_button(self):
        if self.mouse_over_login_button:
            pygame.draw.rect(self._display, (206, 243, 245), self.login_button)
        pygame.draw.rect(self._display, (0, 0, 0), self.login_button, 2)
        self._display.blit(self.login_button.text,
                          (self.login_button.rect.x + 10, self.login_button.rect.y))

    def draw_create_user_button(self):
        if self.mouse_over_create_user_button:
            pygame.draw.rect(self._display, (206, 243, 245), self.create_user_button)
        pygame.draw.rect(self._display, (0, 0, 0), self.create_user_button, 2)
        self._display.blit(self.create_user_button.text,
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

    def set_error_message(self, message):
        self.error_message = Error(text = message, 
            center = self._display.get_rect().center)

    def make_login_page_empty(self):
        self.username = ""
        self.password = ""
        self.mouse_over_login_button = False
        self.mouse_over_create_user_button = False
