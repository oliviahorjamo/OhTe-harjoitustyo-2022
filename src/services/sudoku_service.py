#tämä moduuli vastaa sovelluslogiikasta

class SudokuService:

    def __init__(self, sudoku_repository, user_repository):

        self._user = None
        self._sudoku_repository = sudoku_repository
        self._user_repository = user_repository

    def login(self, username, password):
        pass

    def create_user(self, username, password, login = True):
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            pass
        