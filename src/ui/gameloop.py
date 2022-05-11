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
        self.write_password = False
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

            show_sudoku_id = self.mainpage.select_sudoku(
                pygame.mouse.get_pos()
            )

            if show_sudoku_id != None:
                self.mainpage.underline_sudoku = show_sudoku_id

                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.show_sudoku = True
                        self.show_mainpage = False
                        self.view_sudoku = ViewSudoku(show_sudoku_id)
                        self._renderer.current_view = self.view_sudoku

            else:
                self.mainpage.underline_sudoku = None

            if self.mainpage.logout_button_collide(pygame.mouse.get_pos()):
                self.mainpage.mouse_over_logout = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sudoku_service.logout()
                    self.show_mainpage = False
                    self.show_login = True
                    self._renderer.current_view = login_view
            else:
                self.mainpage.mouse_over_logout = False

            if event.type == pygame.QUIT:
                return False

    def _handle_events_login(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.login_view.username_field_collide(pygame.mouse.get_pos()):
                    self.write_username = True
                    self.login_view.write_username = True
                    self.login_view.error_happened = False
                else:
                    self.write_username = False
                    self.login_view.write_username = False
                if self.login_view.password_field_collide(pygame.mouse.get_pos()):
                    self.write_password = True
                    self.login_view.write_password = True
                    self.login_view.error_happened = False
                else:
                    self.write_password = False
                    self.login_view.write_password = False
                if self.login_view.login_button_collide(pygame.mouse.get_pos()) and len(self.login_view.username) > 0 and len(self.login_view.password) > 0:
                    try:
                        sudoku_service.login(
                            username=self.login_view.username, password=self.login_view.password)
                        self.show_login = False
                        self.show_mainpage = True
                        self._renderer.current_view = self.mainpage
                        self.login_view.make_login_page_empty()
                    except InvalidCredentialsError:
                        message = "Väärä käyttäjänimi tai salasana"
                        self.login_view.error_happened = True
                        self.login_view.set_error_message(message)

                if self.login_view.create_user_button_collide(pygame.mouse.get_pos()) and len(self.login_view.username) > 0 and len(self.login_view.password) > 0:
                    try:
                        sudoku_service.create_user(
                            username=self.login_view.username, password=self.login_view.password)
                        self.show_login = False
                        self.show_mainpage = True
                        self._renderer.current_view = self.mainpage
                        self.login_view.make_login_page_empty()
                    except UsernameExistsError:
                        message = "Tällä käyttäjänimellä on jo käyttäjä"
                        self.login_view.error_happened = True
                        self.login_view.set_error_message(message)

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

            if self.login_view.login_button_collide(pygame.mouse.get_pos()):
                self.login_view.mouse_over_login = True
            else:
                self.login_view.mouse_over_login = False

            if self.login_view.create_user_button_collide(pygame.mouse.get_pos()):
                self.login_view.mouse_over_create_user = True
            else:
                self.login_view.mouse_over_create_user = False

            if event.type == pygame.QUIT:
                return False

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

            if self.view_sudoku.logout_button_collide(pygame.mouse.get_pos()):
                self.view_sudoku.mouse_over_logout = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sudoku_service.logout()
                    self.show_sudoku = False
                    self.show_login = True
                    self._renderer.current_view = login_view
            else:
                self.view_sudoku.mouse_over_logout = False

            if self.view_sudoku.back_button_collide(pygame.mouse.get_pos()):
                self.view_sudoku.mouse_over_backbutton = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.show_sudoku = False
                    self.show_mainpage = True
                    self._renderer.current_view = mainpage
            else:
                self.view_sudoku.mouse_over_backbutton = False

            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
