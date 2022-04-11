# tämä moduuli vastaa sovelluslogiikasta

#tähän alkuun repositorioiden importtaaminen myöhemmin

class SudokuService:

    def __init__(self):

        self._user = None
        #self._sudoku_repository = sudoku_repository
        #self._user_repository = user_repository

    def login(self, username, password):
        pass

    def create_user(self, username, password, login=True):
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            pass

    def add_number(self, originals, sudoku, row, column, number):
        if self.test_square_empty(originals, sudoku, row, column):
            sudoku.grid[row][column] = number
            return True
        else:
            return False

    def delete_number(self, originals, sudoku, row, column):
        if self.test_can_delete(originals, sudoku, row, column):
            sudoku.grid[row][column] = 0
            return True
        return False

    def test_square_empty(self, originals, sudoku, row, column):
        if sudoku.grid[row][column] == 0 and originals[row][column] == 0:
            return True
        return False

    def test_can_delete(self, originals, sudoku, row, column):
        #testaa että numero on itse lisätty
        if originals[row][column] == 0:
            return True
        return False

sudoku_service = SudokuService()