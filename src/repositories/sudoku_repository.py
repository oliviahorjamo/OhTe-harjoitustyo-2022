# Tästä tulee repositoriot alkuperäisten sudokujen lisäämiselle ja muokatuille sudokuille

from pathlib import Path
from config import ORIGINALS_FILE_PATH, SUDOKUS_FILE_PATH
from entities.sudoku import OriginalSudoku, Sudoku


class OriginalSudokuRepository:
    # lukee alkuperäset sudokut jotka lisätään käsin
    def __init__(self, file_path):
        self.file_path = file_path

    def ensure_file_exists(self):
        Path(self.file_path).touch()

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

    def delete_all(self):
        self._write([])

    def _write(self, originals):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for original_sudoku in originals:
                row = f"""{original_sudoku.id};{str(original_sudoku.grid[0])[1:-1]};{str(original_sudoku.grid[1])[1:-1]};{str(original_sudoku.grid[2])[1:-1]};{str(original_sudoku.grid[3])[1:-1]};{str(original_sudoku.grid[4])[1:-1]};{str(original_sudoku.grid[5])[1:-1]};{str(original_sudoku.grid[6])[1:-1]};{str(original_sudoku.grid[7])[1:-1]};{str(original_sudoku.grid[8])[1:-1]}"""
                file.write(row+"\n")
                    
    def create(self, original_sudoku):
        originals = self.find_all()
        originals.append(original_sudoku)
        self._write(originals)
        return original_sudoku


class SudokuRepository:
    # lukee käyttäjän id:n ja alkuperäsen sudokun id:n mukaan käyttäjän keskeneräisiä sudokuja
    # tallentaa keskeneräisiä sudokuja
    def __init__(self, file_path):
        self.file_path = file_path

sudoku_repository = SudokuRepository(SUDOKUS_FILE_PATH)
original_sudokus_repository = OriginalSudokuRepository(ORIGINALS_FILE_PATH)