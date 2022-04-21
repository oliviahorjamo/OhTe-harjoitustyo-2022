import pygame
from ui.clock import Clock
from ui.renderer import Renderer
from ui.view_mainpage import mainpage
from ui.view_sudoku import ViewSudoku

class GameLoop:

    def __init__(self):
        self.mainpage = mainpage
        #self.view_sudoku = view_sudoku
        self.clock = Clock()
        self._cell_size = 33

    def start(self):
        self._renderer = Renderer(self.mainpage.display)
        while True:
            if self._handle_events() == False:
                break

            #current_time = self.clock.get_ticks()
            #self.view_sudoku.update(current_time)
            self._render_mainpage()
            self.clock.tick(60)

    def start_sudoku_view(self):
        self._renderer = Renderer(self.view_sudoku.display, self.view_sudoku)
        while True:
            if self._handle_events() == False:
                break

            self._render_sudoku()

            if self.view_sudoku.is_completed():
                break

            self.clock.tick(60)
        


    def _handle_events(self):
        for event in pygame.event.get():

                #TODO lisää tähän kans hiiren käsittelyt jotta
                #saadaan siirtymät mainpagelta eteenpäin
                #hiirellä klikkaaminen asettaa start gamen trueksi
                #sit näytetään kyseinen sudoku

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    show_sudoku_id = self.mainpage.select_sudoku(pygame.mouse.get_pos())
                    if show_sudoku_id != None:
                        self.show_sudoku = True
                        self.view_sudoku = ViewSudoku(show_sudoku_id)
                        self.start_sudoku_view()

            if event.type == pygame.KEYDOWN:

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

            elif event.type == pygame.QUIT:
                return False

    def _render_mainpage(self):
        self._renderer.render_mainpage()

    def _render_sudoku(self):
        self._renderer.render_sudoku()
