import pygame
from ui.clock import Clock
from ui.renderer import Renderer
from ui.view_mainpage import mainpage
from ui.view_sudoku import ViewSudoku
from ui.view_login import login_view
from services.sudoku_service import InvalidCredentialsError, UsernameExistsError, sudoku_service


class GameLoop:
    """Käyttöliittymän käsittelystä vastaava luokka.
    """

    def __init__(self):
        self.mainpage = mainpage
        self.login_view = login_view
        self.clock = Clock()
        self.show_login = False
        self.show_sudoku = False
        self.show_mainpage = False
        self._cell_size = 33
        self.write_username = False
        self.current_view = None
        self._renderer = Renderer(display=self.login_view.display)

    def run(self):
        while True:
            if self._handle_events() == False:
                break
            self._render()
            self.clock.tick(60)

    def _handle_events(self):
        if self.show_login:
            return self._handle_events_login()
        if self.show_mainpage:
            return self._handle_events_mainpage()
        if self.show_sudoku:
            return self._handle_events_sudoku()

    def _handle_events_mainpage(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                show_sudoku_id = self.mainpage.select_sudoku(
                    pygame.mouse.get_pos())
                if show_sudoku_id != None:
                    self.show_sudoku = True
                    self.show_mainpage = False
                    self.view_sudoku = ViewSudoku(show_sudoku_id)
                    self._renderer.current_view = self.view_sudoku

    def _handle_events_login(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.login_view.username_field_collide(pygame.mouse.get_pos()):
                    self.write_username = True
                else:
                    self.write_username = False
                if self.login_view.password_field_collide(pygame.mouse.get_pos()):
                    self.write_password = True
                else:
                    self.write_password = False
                if self.login_view.login_button_collide(pygame.mouse.get_pos()) and len(self.login_view.username) > 0 and len(self.login_view.password) > 0:
                    try:
                        sudoku_service.login(
                            username=self.login_view.username, password=self.login_view.password)
                        self.show_login = False
                        self.show_mainpage = True
                        self._renderer.current_view = self.mainpage
                    except InvalidCredentialsError:
                        print("väärä käyttäjänimi tai salasana")

                if self.login_view.create_user_button_collide(pygame.mouse.get_pos()) and len(self.login_view.username) > 0 and len(self.login_view.password) > 0:
                    try:
                        sudoku_service.create_user(
                            username=self.login_view.username, password=self.login_view.password)
                        self.show_login = False
                        self.show_mainpage = True
                        self._renderer.current_view = self.mainpage
                    except UsernameExistsError:
                        print("tällä käyttäjänimellä on jo käyttäjä")

            if event.type == pygame.KEYDOWN:
                if self.write_username == True:
                    if event.key == pygame.K_BACKSPACE:
                        self.login_view.username = self.login_view.username[:-1]
                    else:
                        self.login_view.username += event.unicode
                if self.write_password == True:
                    if event.key == pygame.K_BACKSPACE:
                        self.login_view.password = self.login_view.password[:-1]
                    else:
                        self.login_view.password += event.unicode

    def _handle_events_sudoku(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.view_sudoku.move(dx=- self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self.view_sudoku.move(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self.view_sudoku.move(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self.view_sudoku.move(dy=self._cell_size)

                char = event.unicode
                try:
                    if 0 < int(char) < 10:
                        self.view_sudoku.add_number((int(char)))
                except ValueError:
                    pass

                if event.key == pygame.K_DELETE:
                    self.view_sudoku.delete_number()

            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
