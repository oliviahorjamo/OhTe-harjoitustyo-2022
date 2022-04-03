#sisältää sudokun pelilogiikan testit
#3.4.2022 pelilogiikkaa ei vielä lainkaan SudokuService -luokassa vaan pelkästään index.py tiedostossa
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
print(sys.path)

import unittest
from entities.sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        #sudoku on nyt moduuli
        print("ollaan setupissa")
        self.sudoku = Sudoku(1)

    def test_create_sudoku(self):
        self.assertEqual(str(self.sudoku.grid), str([
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]))
