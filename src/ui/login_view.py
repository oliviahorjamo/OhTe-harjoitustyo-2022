
import pygame
from ui.sprites import EnterTextField, Button, Error
from ui.general_ui import GeneralUIDrawing


class LoginView:
    def __init__(self, display):
        self._display = display
        self._general_ui = GeneralUIDrawing(self._display)
        self.username = ""
        self.password = ""
        self.username_field_clicked = False
        self.password_field_clicked = False
        self.mouse_over_login_button = False
        self.mouse_over_create_user_button = False
        self.error_happened = False
        self._all_sprites = pygame.sprite.Group()
        self._initialize_sprites()

    def _initialize_sprites(self):
        self._username_field = EnterTextField(
            x=self._display.get_width() / 4, y=50)
        self._password_field = EnterTextField(
            x=self._display.get_width() / 4, y=100)
        self._login_button = Button(
            text="Log in", x=self._display.get_width() / 4, y=150)
        self._create_user_button = Button(
            text="Create user", x=self._display.get_width() / 4, y=200)
        self._all_sprites.add(self._username_field, self._password_field,
                             self._login_button, self._create_user_button)

    def draw(self):
        self._display.fill((255, 255, 255))
        self.draw_login_fields()
        self.draw_buttons()
        if self.error_happened:
            self.draw_error_message()

    def draw_error_message(self):
        self._display.blit(self.error_message.text, self.error_message.rect)

    def draw_login_fields(self):
        self._general_ui.draw_text_field(field = self._username_field, description="Käyttäjänimi",
        text = self.username, field_clicked=self.username_field_clicked)
        self._general_ui.draw_text_field(field = self._password_field, description="Salasana",
        text = self.password, field_clicked=self.password_field_clicked)

    def draw_buttons(self):
        self._general_ui.draw_button(button = self._login_button,
        mouse_over_button=self.mouse_over_login_button)
        self._general_ui.draw_button(button=self._create_user_button,
        mouse_over_button=self.mouse_over_create_user_button)

    def username_field_collide(self, mouse):
        if self._username_field.rect.collidepoint(mouse):
            return True

    def password_field_collide(self, mouse):
        if self._password_field.rect.collidepoint(mouse):
            return True

    def login_button_collide(self, mouse):
        if self._login_button.rect.collidepoint(mouse):
            return True

    def create_user_button_collide(self, mouse):
        if self._create_user_button.rect.collidepoint(mouse):
            return True

    def set_error_message(self, message):
        self.error_message = Error(text = message, 
            center = self._display.get_rect().center)

    def make_login_page_empty(self):
        self.username = ""
        self.password = ""
        self.mouse_over_login_button = False
        self.mouse_over_create_user_button = False
