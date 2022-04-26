# sisältää sudokun pelilogiikan testit
import unittest
import sys
import os
from services.sudoku_service import SudokuService, InvalidCredentialsError, UsernameExistsError
from entities.sudoku import Sudoku, OriginalSudoku
from entities.user import User
from repositories.sudoku_repository import original_sudokus_repository, sudoku_repository


class TestSudoku(unittest.TestCase):
    def setUp(self):
        original_sudokus_repository.delete_all()
        self.sudoku_service = SudokuService()
        self.user_testi1 = User(username="testi1", password="testi1")
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

    def login_user(self, user):
        self.sudoku_service.create_user(self.user.username, self.user.password)

   # def test_login_with_valid_username_and_password(self):
    #    self.sudoku_service.create_user(
     #   self.user_testi1.username,
      #  self.user_testi1.password,
       # login = False
        # )

   #     user = self.sudoku_service.login(
    #        self.user_testi1.username,
     #       self.user_testi1.password
      #  )

       # self.assertEqual(user.username, self.user_testi1.username)

    def test_login_with_invalid_username(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.sudoku_service.login('testing', 'invalid')
        )

 #   def test_login_with_invalid_password(self):
  #      self.sudoku_service.create_user(username=self.user_testi1.username, password=self.user_testi1.password, login = False)
   #     self.assertRaises(
    #        InvalidCredentialsError,
     #       lambda: self.sudoku_service.login(username = self.user_testi1, password ="test")
      #  )

    def test_create_user_with_existing_username(self):
        self.sudoku_service.create_user(self.user_testi1.username, 'testing')
        self.assertRaises(
            UsernameExistsError,
            lambda: self.sudoku_service.create_user(
                self.user_testi1.username, 'random')
        )
