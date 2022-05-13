import pygame
from ui.clock import Clock
from ui.renderer import Renderer
from ui.mainpage_view import MainpageView
from ui.sudoku_view import SudokuView
from ui.login_view import LoginView
from services.sudoku_service import InvalidCredentialsError, UsernameExistsError, InvalidUsernameError, InvalidPasswordError,sudoku_service


class GameLoop:
    """Käyttöliittymän käsittelystä vastaava luokka.
    """

    def __init__(self, display):
        """Luokan konstruktori, joka luo uuden GameLoop -objektin

        Args:
            display: Käyttöliittymän aloituksessa luotu näyttö, joka injektoidaan
            parametrina käyttöliittymän eri näkymille.
        """
        self._sudoku_service = sudoku_service
        self._show_login_view = False
        self._show_sudoku_view = False
        self._show_mainpage_view = False
        self._display = display
        self._clock = Clock()
        self._renderer = Renderer()
        self._mainpage_view = MainpageView(display = self._display)
        self._login_view = LoginView(display = self._display)
        self.set_current_view(self._login_view)

    def set_current_view(self, new_view, old_view = None):
        """Asettaa uuden näkymän rendererille ja asettaa tiedon siitä, minkä
        näkymän syötettä vastaanotetaan.

        Args:
            view: Näkymä, johon siirrytään
        """
        self._renderer.current_view = new_view
        if isinstance(new_view, LoginView):
            self._show_login_view = True
        elif isinstance(new_view, MainpageView):
            self._show_mainpage_view = True
        elif isinstance(new_view, SudokuView):
            self._show_sudoku_view = True
        self.hide_old_view(old_view=old_view)

    def hide_old_view(self, old_view):
        """Asettaa GameLoopille tiedon, että lakataan käsittelemästä kyseiseen
        näkymään liittyvää syötettä.

        Args:
            current_view: Nykyinen näkymä, joka piilotetaan.
        """
        if isinstance(old_view, LoginView):
            self._show_login_view = False
            self._login_view.make_login_page_empty()
        elif isinstance(old_view, MainpageView):
            self._show_mainpage_view = False
        elif isinstance(old_view, SudokuView):
            self._show_sudoku_view = False

    def run(self):
        """Kutsuu näytön päivittämistä ja syötteen käsittelyä niin kauan, kunnes
        käyttäjä sulkee pelinäytön.
        """
        while True:
            if self._handle_events() == False:
                break
            self._render()
            self._clock.tick(60)

    def _handle_events(self):
        """Kutsuu nykyisen näkymän syötteen käsittelystä vastaavaa funktiota.

        Returns:
            Ei mitään tai mahdollisesti False, jos käyttäjä on painanut pelin
            sulkevaa painiketta.
        """
        if self._show_login_view:
            return self._handle_events_login_view()
        if self._show_mainpage_view:
            return self._handle_events_mainpage_view()
        if self._show_sudoku_view:
            return self._handle_events_sudoku_view()

    def _handle_events_login_view(self):
        """Käsittelee käyttäjän syötettä, kun ollaan kirjautumissivulla.

        Returns:
            Ei mitään tai mahdollisesti False, jos käyttäjä on painanut pelin
            sulkevaa painiketta.
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self._login_view.username_field_collide(pygame.mouse.get_pos()):
                    self._login_view.username_field_clicked = True
                    self._login_view.error_happened = False
                else:
                    self._login_view.username_field_clicked = False
                if self._login_view.password_field_collide(pygame.mouse.get_pos()):
                    self._login_view.password_field_clicked = True
                    self._login_view.error_happened = False
                else:
                    self._login_view.password_field_clicked = False

                if self._login_view.login_button_collide(pygame.mouse.get_pos()):
                    try:
                        self._sudoku_service.login(
                            username=self._login_view.username, password=self._login_view.password)
                        self.set_current_view(new_view=self._mainpage_view, old_view=self._login_view)
                    except InvalidCredentialsError:
                        error_message = "Väärä käyttäjänimi tai salasana"
                        self._login_view.error_happened = True
                        self._login_view.set_error_message(error_message)
                    except InvalidUsernameError:
                        error_message = "Käyttäjänimi pitää olla 1-19 merkkiä"
                        self._login_view.error_happened = True
                        self._login_view.set_error_message(error_message)
                    except InvalidPasswordError:
                        error_message = "Salasana pitää olla 1-19 merkkiä"
                        self._login_view.error_happened = True
                        self._login_view.set_error_message(error_message)

                if self._login_view.create_user_button_collide(pygame.mouse.get_pos()):
                    try:
                        self._sudoku_service.create_user(
                            username=self._login_view.username, password=self._login_view.password)
                        self.set_current_view(new_view=self._mainpage_view, old_view=self._login_view)
                    except UsernameExistsError:
                        message = "Tällä käyttäjänimellä on jo käyttäjä"
                        self._login_view.error_happened = True
                        self._login_view.set_error_message(message)
                    except InvalidUsernameError:
                        error_message = "Käyttäjänimi pitää olla 1-19 merkkiä"
                        self._login_view.error_happened = True
                        self._login_view.set_error_message(error_message)
                    except InvalidPasswordError:
                        error_message = "Salasana pitää olla 1-19 merkkiä"
                        self._login_view.error_happened = True
                        self._login_view.set_error_message(error_message)

            if event.type == pygame.KEYDOWN:

                if self._login_view.username_field_clicked == True:
                    if event.key == pygame.K_BACKSPACE:
                        self._login_view.username = self._login_view.username[:-1]
                    else:
                        self._login_view.username += event.unicode
                if self._login_view.password_field_clicked == True:
                    if event.key == pygame.K_BACKSPACE:
                        self._login_view.password = self._login_view.password[:-1]
                    else:
                        self._login_view.password += event.unicode

            if self._login_view.login_button_collide(pygame.mouse.get_pos()):
                self._login_view.mouse_over_login_button = True
            else:
                self._login_view.mouse_over_login_button = False

            if self._login_view.create_user_button_collide(pygame.mouse.get_pos()):
                self._login_view.mouse_over_create_user_button = True
            else:
                self._login_view.mouse_over_create_user_button = False

            if event.type == pygame.QUIT:
                return False

    def _handle_events_mainpage_view(self):
        """Käsittelee käyttäjän syötettä, kun ollaan etusivulla.

        Returns:
            Ei mitään tai mahdollisesti False, jos käyttäjä on painanut pelin
            sulkevaa painiketta.
        """
        for event in pygame.event.get():

            selected_sudoku_id = self._mainpage_view.select_sudoku(
                pygame.mouse.get_pos()
            )

            if selected_sudoku_id != None:
                self._mainpage_view.underlined_sudoku = selected_sudoku_id
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self._sudoku_view = SudokuView(original_sudoku_id = selected_sudoku_id, display = self._display)
                        self.set_current_view(old_view=self._mainpage_view, new_view=self._sudoku_view)
            else:
                self._mainpage_view.underlined_sudoku = None

            if self._mainpage_view.logout_button_collide(pygame.mouse.get_pos()):
                self._mainpage_view.mouse_over_logout_button = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._sudoku_service.logout()
                    self.set_current_view(old_view=self._mainpage_view, new_view=self._login_view)
            else:
                self._mainpage_view.mouse_over_logout_button = False

            if event.type == pygame.QUIT:
                return False

    def _handle_events_sudoku_view(self):
        """Käsittelee käyttäjän syötettä, kun ollaan pelinäkymässä

        Returns:
            Ei mitään tai False, jos käyttäjä on painanut pelin sulkevaa painiketta.
        """
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self._sudoku_view.move(dx=-self._sudoku_view.cell_size)
                elif event.key == pygame.K_RIGHT:
                    self._sudoku_view.move(dx=self._sudoku_view.cell_size)
                elif event.key == pygame.K_UP:
                    self._sudoku_view.move(dy=-self._sudoku_view.cell_size)
                elif event.key == pygame.K_DOWN:
                    self._sudoku_view.move(dy=self._sudoku_view.cell_size)
                elif event.key == pygame.K_DELETE:
                        self._sudoku_view.delete_number()
                else:
                    char = event.unicode
                    try:
                        if 0 < int(char) < 10:
                            self._sudoku_view.add_number((int(char)))
                    except ValueError:
                        pass

            if self._sudoku_view.logout_button_collide(pygame.mouse.get_pos()):
                self._sudoku_view.mouse_over_logout_button = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._sudoku_service.logout()
                    self.set_current_view(old_view=self._sudoku_view, new_view=self._login_view)
            else:
                self._sudoku_view.mouse_over_logout_button = False

            if self._sudoku_view.back_button_collide(pygame.mouse.get_pos()):
                self._sudoku_view.mouse_over_return_button = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.set_current_view(old_view=self._sudoku_view, new_view=self._mainpage_view)
            else:
                self._sudoku_view.mouse_over_return_button = False

            if event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
