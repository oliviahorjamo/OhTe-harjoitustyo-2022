import pygame
from ui.clock import Clock
from ui.renderer import Renderer
from ui.view_mainpage import mainpage
from ui.view_sudoku import ViewSudoku
from ui.view_login import login_view
from services.sudoku_service import InvalidCredentialsError, UsernameExistsError, sudoku_service


class GameLoop:

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
        self._renderer = Renderer(display = self.login_view.display)

    def run(self):
        while True:
            if self._handle_events() == False:
                break
            self._render()
            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and self.show_mainpage == True:
                if pygame.mouse.get_pressed():
                    show_sudoku_id = self.mainpage.select_sudoku(
                        pygame.mouse.get_pos())
                    if show_sudoku_id != None:
                        self.show_sudoku = True
                        self.show_mainpage = False
                        self.view_sudoku = ViewSudoku(show_sudoku_id)
                        self._renderer.current_view = self.view_sudoku

            if self.show_login == True and event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
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

                        # kutsu sudoku servicen login toimintoja jotka kutsuu repositoriota

                    if self.login_view.create_user_button_collide(pygame.mouse.get_pos()) and len(self.login_view.username) > 0 and len(self.login_view.password) > 0:
                        try:
                            sudoku_service.create_user(
                                username=self.login_view.username, password=self.login_view.password)
                            self.show_login = False
                            self.start_mainpage()
                        except UsernameExistsError:
                            print("tällä käyttäjänimellä on jo käyttäjä")

            if event.type == pygame.KEYDOWN and self.show_sudoku == True:

                if event.key == pygame.K_LEFT:
                    self.view_sudoku.move(dx=- self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self.view_sudoku.move(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self.view_sudoku.move(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self.view_sudoku.move(dy=self._cell_size)

                if event.key == pygame.K_1:
                    self.view_sudoku.add_number(1)
                if event.key == pygame.K_2:
                    self.view_sudoku.add_number(2)
                if event.key == pygame.K_3:
                    self.view_sudoku.add_number(3)
                if event.key == pygame.K_4:
                    self.view_sudoku.add_number(4)
                if event.key == pygame.K_5:
                    self.view_sudoku.add_number(5)
                if event.key == pygame.K_6:
                    self.view_sudoku.add_number(6)
                if event.key == pygame.K_7:
                    self.view_sudoku.add_number(7)
                if event.key == pygame.K_8:
                    self.view_sudoku.add_number(8)
                if event.key == pygame.K_9:
                    self.view_sudoku.add_number(9)

                if event.key == pygame.K_DELETE:
                    self.view_sudoku.delete_number()

            if event.type == pygame.KEYDOWN and self.show_login == True:
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

            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()