# Tästä tulee repositoriot alkuperäisten sudokujen lisäämiselle ja muokatuille sudokuille

import os
from entities.sudoku import OriginalSudoku, Sudoku

dirname = os.path.dirname(__file__)


class OriginalSudokuRepository:
    # lukee alkuperäset sudokut jotka lisätään käsin
    def __init__(self, file_path):
        self.file_path = file_path

    def find_all(self):
        return self.read()

    def find_by_id(self, id_number):
        sudokus = self.find_all()
        current_sudoku = filter(
            lambda sudoku: sudoku.id == id_number, sudokus
        )
        return list(current_sudoku)[0]

    def read(self):
        original_sudokus = []
        with open(self.file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                id = int(parts[0])
                grid = []
                for i in range(1, len(parts)):
                    elements = parts[i].split(",")
                    row = []
                    for element in elements:
                        row.append(int(element))
                    grid.append(row)
                original_sudokus.append(OriginalSudoku(id = id, grid = grid))
        return original_sudokus


class SudokuRepository:
    # lukee käyttäjän id:n ja alkuperäsen sudokun id:n mukaan käyttäjän keskeneräisiä sudokuja
    # tallentaa keskeneräisiä sudokuja
    def __init__(self, file_path):
        self.file_path = file_path

original_sudokus_repository = OriginalSudokuRepository(os.path.join(dirname, "..", "data", "originals.csv"))
sudoku_repository = SudokuRepository(os.path.join(dirname, "..", "data", "sudokus.csv"))
