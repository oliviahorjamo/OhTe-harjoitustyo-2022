# sisältää sudokun pelilogiikan testit
import unittest
from services.sudoku_service import InvalidUsernameError, SudokuService, InvalidCredentialsError, UsernameExistsError, InvalidPasswordError
from entities.sudoku import Sudoku, OriginalSudoku
from entities.user import User
from repositories.sudoku_repository import original_sudoku_repository, sudoku_repository
from repositories.user_repository import user_repository


class TestSudokuService(unittest.TestCase):
    def setUp(self):
        original_sudoku_repository.delete_all()
        user_repository.delete_all()
        sudoku_repository.delete_all()
        self.sudoku_service = SudokuService()
        self.user_testi1 = User(username="testi1", password="testi1")
        self.user_testi2 = User(username="testi2", password="testi2")
        self.original_sudoku_1 = OriginalSudoku(id=1, grid=[
            [0, 0, 4, 0, 0, 8, 0, 5, 7],
            [0, 0, 2, 0, 0, 5, 0, 0, 3],
            [5, 1, 0, 0, 7, 0, 0, 8, 4],
            [0, 2, 6, 0, 1, 0, 3, 7, 0],
            [0, 5, 8, 3, 6, 0, 0, 0, 0],
            [0, 0, 0, 8, 2, 9, 0, 6, 0],
            [4, 0, 0, 7, 0, 0, 8, 3, 2],
            [2, 0, 0, 6, 9, 0, 7, 0, 5],
            [0, 0, 0, 4, 8, 0, 0, 9, 0]
        ])
        self.original_sudoku_2 = OriginalSudoku(id=2, grid=[
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 2, 0, 0, 5, 0, 0, 3],
            [5, 1, 0, 0, 7, 0, 0, 8, 4],
            [0, 2, 6, 0, 1, 0, 3, 7, 0],
            [0, 5, 8, 3, 6, 0, 0, 0, 0],
            [0, 0, 0, 8, 2, 9, 0, 6, 0],
            [4, 0, 0, 7, 0, 0, 8, 3, 2],
            [2, 0, 0, 6, 9, 0, 7, 0, 5],
            [0, 0, 0, 4, 8, 0, 0, 9, 0]
        ])
        self.empty_sudoku_1 = Sudoku(
            original_sudoku_id=1
        )

    def login_user(self, user):
        self.sudoku_service.create_user(user.username, user.password)

    def test_login_with_valid_username_and_password(self):
        self.sudoku_service.create_user(
            self.user_testi1.username,
            self.user_testi1.password,
            login=False
        )

        user = self.sudoku_service.login(
            self.user_testi1.username,
            self.user_testi1.password
        )

        self.assertEqual(user.username, self.user_testi1.username)

    def test_login_with_invalid_username(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.sudoku_service.login('testing', 'invalid')
        )

    def test_login_with_invalid_password(self):
        self.sudoku_service.create_user(
            username=self.user_testi1.username, password=self.user_testi1.password, login=False)
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.sudoku_service.login(
                username=self.user_testi1.username, password="test")
        )

    def test_create_user_with_existing_username(self):
        self.sudoku_service.create_user(self.user_testi1.username, 'testing')
        self.assertRaises(
            UsernameExistsError,
            lambda: self.sudoku_service.create_user(
                self.user_testi1.username, 'random')
        )

    def test_find_all_sudokus(self):
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_repository.create(self.original_sudoku_2)
        originals = self.sudoku_service.find_all_sudokus()
        self.assertEqual(len(originals), 2)
        self.assertEqual(originals[0].grid, self.original_sudoku_1.grid)
        self.assertEqual(originals[1].grid, self.original_sudoku_2.grid)

    def test_find_original_sudoku_by_id(self):
        original_sudoku_repository.create(self.original_sudoku_1)
        id = self.original_sudoku_1.id
        found_sudoku = self.sudoku_service.find_original_numbers(id)
        self.assertEqual(found_sudoku.grid, self.original_sudoku_1.grid)

    def test_find_user_sudoku_by_id_when_no_previous_solution(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.assertEqual(user_sudoku.grid, self.empty_sudoku_1.grid)
        self.assertEqual(user_sudoku.user, self.user_testi1.username)

    def test_add_number_when_allowed(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       1, 1, 1)
        self.assertEqual(user_sudoku.grid[1][1], 1)

    def test_find_user_sudoku_by_id_when_previous_solution_exists(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       1, 1, 1)
        user_sudoku_in_repository = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id
        )
        self.assertEqual(
            user_sudoku.grid, user_sudoku_in_repository.grid)

    def test_add_number_when_not_allowed(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       0, 2, 1)
        self.assertEqual(user_sudoku.grid[0][2], 0)

    def test_no_double_accounts_in_repository(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       1, 1, 1)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       0, 1, 1)
        all_sudokus_in_repository = sudoku_repository.read()
        self.assertEqual(len(all_sudokus_in_repository), 1)

    def test_previous_numbers_not_overwritten(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       1, 1, 1)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       0, 1, 1)
        user_sudoku_in_repository = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id
        )
        self.assertEqual(user_sudoku_in_repository.grid[1][1], 1)
        self.assertEqual(user_sudoku_in_repository.grid[0][1], 1)

    def test_delete_number(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku,
                                       1, 1, 1)
        self.sudoku_service.delete_number(self.original_sudoku_1.grid,
                                          sudoku=user_sudoku, row=1, column=1)
        user_sudoku_in_repository = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id
        )
        self.assertEqual(user_sudoku.grid[1][1], 0)
        self.assertEqual(user_sudoku_in_repository.grid[1][1], 0)

    def test_cant_delete_original_number(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.delete_number(original_numbers=self.original_sudoku_1.grid,
                                          sudoku=user_sudoku, row=0, column=2)
        original_sudoku_in_repository = self.sudoku_service.find_original_numbers(
            original_sudoku_id=original_sudoku_id
        )
        self.assertEqual(original_sudoku_in_repository.grid[0][2], 4)

    def test_other_users_solutions_not_deleted(self):
        self.login_user(self.user_testi1)
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_id = self.original_sudoku_1.id
        user_sudoku_1 = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku_1,
                                       1, 1, 1)
        self.login_user(self.user_testi2)
        user_sudoku_2 = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.sudoku_service.add_number(self.original_sudoku_1.grid, user_sudoku_2,
                                       1, 1, 2)
        user_repository.delete_all()
        self.login_user(self.user_testi1)
        user_1_sudoku_in_repository = self.sudoku_service.find_added_numbers(
            original_sudoku_id=original_sudoku_id)
        self.assertEqual(user_1_sudoku_in_repository.grid[1][1], 1)

    def test_too_long_username_when_creating_user(self):
        user = User(username="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    password="jee")
        self.assertRaises(
            InvalidUsernameError,
            lambda: self.sudoku_service.create_user(
                user.username, user.password)
        )

    def test_too_long_password_when_creating_user(self):
        user = User(username="jee",
                    password="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertRaises(
            InvalidPasswordError,
            lambda: self.sudoku_service.create_user(
                user.username, user.password)
        )

    def test_logout(self):
        self.login_user(self.user_testi1)
        self.sudoku_service.logout()
        self.assertEqual(self.sudoku_service._user, None)
