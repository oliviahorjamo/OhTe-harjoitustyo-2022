import unittest
from repositories.sudoku_repository import sudoku_repository, original_sudoku_repository
from repositories.user_repository import user_repository
from entities.sudoku import OriginalSudoku, Sudoku
from entities.user import User


class TestOriginalSudokuRepository(unittest.TestCase):
    def setUp(self):
        original_sudoku_repository.delete_all()
        user_repository.delete_all()
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

    def test_create(self):
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudokus = original_sudoku_repository.find_all()
        self.assertEqual(len(original_sudokus), 1)
        self.assertEqual(original_sudokus[0].grid, self.original_sudoku_1.grid)

    def test_find_all(self):
        original_sudoku_repository.create(self.original_sudoku_1)
        original_sudoku_repository.create(self.original_sudoku_2)
        originals = original_sudoku_repository.find_all()
        self.assertEqual(len(originals), 2)
        self.assertEqual(originals[0].grid, self.original_sudoku_1.grid)
        self.assertEqual(originals[1].grid, self.original_sudoku_2.grid)

    def test_find_by_id(self):
        original_sudoku_repository.create(self.original_sudoku_2)
        sudoku = original_sudoku_repository.find_by_id(2)
        self.assertEqual(sudoku.grid, self.original_sudoku_2.grid)

    def test_delete_all(self):
        original_sudoku_repository.create(self.original_sudoku_1)
        originals = original_sudoku_repository.find_all()
        self.assertEqual(len(originals), 1)
        original_sudoku_repository.delete_all()
        originals = original_sudoku_repository.find_all()
        self.assertEqual(len(originals), 0)


class TestSudokuRepository(unittest.TestCase):
    def setUp(self):
        sudoku_repository.delete_all()
        self.user1 = User(username="testi", password="testi")
        self.user2 = User(username="testi2", password="testi2")
        self.empty_sudoku_1 = Sudoku(original_sudoku_id=1, grid=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], user=self.user1
        )
        self.empty_sudoku_2 = Sudoku(original_sudoku_id=2, grid=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ], user=self.user2
        )

    def test_write_new_numbers(self):
        sudoku_repository.write_new_numbers(self.empty_sudoku_1)
        self.assertEqual(len(sudoku_repository.find_all()), 1)
