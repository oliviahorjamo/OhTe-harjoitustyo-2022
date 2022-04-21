# tämä moduuli vastaa sovelluslogiikasta
# tähän alkuun repositorioiden importtaaminen myöhemmin

from repositories.sudoku_repository import original_sudokus_repository, sudoku_repository
#from entities.sudoku import OriginalSudoku, Sudoku

class SudokuService:

    def __init__(self):
        self._user = None

    def login(self, username, password):
        pass

    def create_user(self, username, password, login=True):
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            pass

    def find_original_numbers(self, original_numbers_id):
        return original_sudokus_repository.find_by_id(original_numbers_id)

    def add_number(self, originals, sudoku, row, column, number):
        if self.test_square_empty(originals, sudoku, row, column):
            sudoku.grid[row][column] = number
            return True
        return False

    def delete_number(self, originals, sudoku, row, column):
        if self.test_can_delete(originals, row, column):
            sudoku.grid[row][column] = 0
            return True
        return False

    def test_square_empty(self, originals, sudoku, row, column):
        if sudoku.grid[row][column] == 0 and originals[row][column] == 0:
            return True
        return False

    def test_can_delete(self, originals, row, column):
        if originals[row][column] == 0:
            return True
        return False

    def find_all_sudokus(self):
        return original_sudokus_repository.find_all()


sudoku_service = SudokuService()
