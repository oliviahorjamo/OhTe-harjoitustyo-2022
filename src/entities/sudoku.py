class OriginalSudoku:
    """Luokka, jonka avulla käsitellään valmiita netistä haettuja sudoku -pohjia.

    Attributes:
        id: sudokulle määritelty id -numero, jonka avulla sudokut yksilöidään
        grid: sudokun valmiit numerot (haetaan repositorion avulla csv -tiedostosta)
    """

    def __init__(self, id, grid):
        """Luokan konstruktori, joka luo uuden alkuperäisen sudokun

        Args:
            id: repositoriosta haettu sudokun yksilöivä id -numero
            grid: repositoriosta haetut alkuperäiset numerot
        """

        self.id = id
        self.grid = grid


class Sudoku:
    """Luokka, jonka avulla käsitellään käyttäjän lisäämiä numeroita.

    Attributes:
        original_sudoku: OriginalSudoku -luokan olio, joka sisältää alkuperäiset numerot
        grid: ruudukko, joka sisältää käyttäjän lisäämät numerot (alussa tyhjä)
    """

    def __init__(self, original_sudoku_id, grid = None, user = None):
        """Luokan konstruktori, joka luo uuden tyhjän sudokupohjan.

        Args:
            original_sudoku: OriginalSudoku -luokan olio, jonka avulla käyttäjän lisäämät numerot
            yhdistetään oikeaan alkuperäiseen sudokuun.
        """

        self.original_sudoku_id = original_sudoku_id
        #self.original_sudoku = original_sudoku
        if grid == None:
            self.grid = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        else:
            self.grid = grid
        self.user = user
