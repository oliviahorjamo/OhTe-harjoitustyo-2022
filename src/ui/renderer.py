import pygame
#from ui.view_sudoku import view_sudoku
#from ui.view_mainpage import mainpage
#from ui.view_login import login_view


class Renderer:
    def __init__(self, display, view_sudoku=None, mainpage=None, login_view=None):
        self._display = display
        self.mainpage = mainpage
        self.login_view = login_view
        self.view_sudoku = view_sudoku

    def render_sudoku(self):
        self._display.fill((255, 255, 255))
        self.view_sudoku.all_sprites.draw(self._display)

        self.view_sudoku.draw_original_numbers(self._display)
        self.view_sudoku.draw_added_numbers(self._display)
        self.view_sudoku.draw_lines(self._display)
        self.view_sudoku.draw_selected_square()

        pygame.display.update()

    def render_mainpage(self):
        # olisko kaikki piirtämiset parempi tehä gameloopissa?
        self._display.fill((255, 255, 255))
        self.mainpage.draw_text(self._display)
        self.mainpage.draw_sudoku_list(self._display)
        #print("ollaan mainpagen renderöinnissiä")
        pygame.display.update()

    def render_login_view(self):
        self._display.fill((255, 255, 255))
        self.login_view.draw_login_fields()
        self.login_view.draw_login_button()
        self.login_view.draw_create_user_button()
        pygame.display.update()
