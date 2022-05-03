# tämä moduuli vastaa sovelluslogiikasta
# tähän alkuun repositorioiden importtaaminen myöhemmin

from repositories.sudoku_repository import original_sudokus_repository, sudoku_repository
from repositories.user_repository import user_repository
#from entities.sudoku import OriginalSudoku, Sudoku
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class SudokuService:

    def __init__(self):
        self._user = None
        self._user_repository = user_repository
        self.original_sudokus_repository = original_sudokus_repository
        self.sudoku_repository = sudoku_repository

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError('Invalid username or password')
        self._user = user
        return user

    def create_user(self, username, password, login=True):
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user

    def find_original_numbers(self, original_numbers_id):
        return self.original_sudokus_repository.find_by_id(original_numbers_id)

    def find_added_numbers(self, original_numbers_id):
        return self.sudoku_repository.find_by_id_and_user(original_numbers_id, self._user.username)

    def add_number(self, originals, sudoku, row, column, number):
        if self.test_square_empty(originals, sudoku, row, column):
            sudoku.grid[row][column] = number
            self.sudoku_repository.delete_old_numbers(original_sudoku_id=sudoku.original_sudoku_id, user_name=self._user.username)
            self.sudoku_repository.write_new_numbers(sudoku)
            return True
        return False

    def delete_number(self, originals, sudoku, row, column):
        if self.test_can_delete(originals, row, column):
            sudoku.grid[row][column] = 0
            self.sudoku_repository.delete_old_numbers(original_sudoku_id=sudoku.original_sudoku_id, user_name=self._user.username)
            self.sudoku_repository.write_new_numbers(sudoku)
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
        return self.original_sudokus_repository.find_all()


sudoku_service = SudokuService()
