
class Sudoku:
    #sudoku tarkoittaa alkuperäisiä ylläpitäjän luomia sudokuita

    #sudoku -luokan oliolla tietty id, jolla tallennetaan alkuperäiset numerot kun uudet pelaajat tallentaa keskeneräisiä vastauksia
    
    #myöhemmin metodit erikseen numeroiden lisäämiselle

    def __init__(self, id):
        self.id = id

        #default grid
        #myöhemmin oma funktionsa sudokun luomiselle

        self.grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

    def add_number(self):
        #lisää uuden numeron
        pass

    def check_validity(self):
        #tarkistaa onko validi
        pass

    def remove_number(self):
        #poistaa asetetun numeron
        #voi käyttää vain itse lisäämiinsä
        pass


class SudokuModified(Sudoku):
    #tää olis käyttäjän uusi sudoku jota muokataan, perii alkuperäisen "stabiilin sudokun"
    #jos toteutetaan näin, kaikki Sudoku -luokan metodit olis tän luokan metodeja
    pass
