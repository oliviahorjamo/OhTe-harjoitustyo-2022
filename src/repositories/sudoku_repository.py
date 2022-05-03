# Tästä tulee repositoriot alkuperäisten sudokujen lisäämiselle ja muokatuille sudokuille

from pathlib import Path
from config import ORIGINALS_FILE_PATH, SUDOKUS_FILE_PATH
from entities.sudoku import OriginalSudoku, Sudoku
import os


class OriginalSudokuRepository:
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
                sudoku_id = int(parts[0])
                grid = []
                for i in range(1, len(parts)):
                    elements = parts[i].split(",")
                    row = []
                    for element in elements:
                        row.append(int(element))
                    grid.append(row)
                original_sudokus.append(OriginalSudoku(id=sudoku_id, grid=grid))
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
    def __init__(self, file_path):
        self.file_path = file_path

    def ensure_file_exists(self):
        Path(self.file_path).touch()


    def find_all(self):
        return self.read()

    def find_by_id_and_user(self, original_sudoku_id, user_name):
        sudokus = self.find_all()
        self.original_sudoku_id = original_sudoku_id
        self.user_name = user_name
        current_sudoku = filter(self._filtering_function, sudokus)
        try:
            return list(current_sudoku)[0]
        except:
            return Sudoku(original_sudoku_id=self.original_sudoku_id)

    def _filtering_function(self, sudoku):
        if sudoku.original_sudoku_id == self.original_sudoku_id and sudoku.user == self.user_name:
            return True
        return False

    def read(self):
        sudokus = []
        with open(self.file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                original_sudoku_id = int(parts[0])
                user_name = parts[1]
                grid = []
                for i in range(2, len(parts)):
                    elements = parts[i].split(",")
                    row = []
                    for element in elements:
                        row.append(int(element))
                    grid.append(row)
                sudokus.append(Sudoku(original_sudoku_id=original_sudoku_id, grid=grid, user = user_name))
        return sudokus

    def delete_all(self):
        self._write([])

    def _write(self, sudokus):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for sudoku in sudokus:
                row = f"""{sudoku.id};{str(sudoku.grid[0])[1:-1]};{str(sudoku.grid[1])[1:-1]};{str(sudoku.grid[2])[1:-1]};{str(sudoku.grid[3])[1:-1]};{str(sudoku.grid[4])[1:-1]};{str(sudoku.grid[5])[1:-1]};{str(sudoku.grid[6])[1:-1]};{str(sudoku.grid[7])[1:-1]};{str(sudoku.grid[8])[1:-1]}"""
                file.write(row+"\n")

    def delete_old_numbers(self, original_sudoku_id, user_name):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for line in lines:
                if f"{original_sudoku_id};{user_name}" not in line.strip("\n"):
                    file.write(line)

    def write_new_numbers(self, sudoku):
        with open(self.file_path, "a", encoding="utf-8") as file:
            row = f"""{sudoku.original_sudoku_id};{str(sudoku.user)};{str(sudoku.grid[0])[1:-1]};{str(sudoku.grid[1])[1:-1]};{str(sudoku.grid[2])[1:-1]};{str(sudoku.grid[3])[1:-1]};{str(sudoku.grid[4])[1:-1]};{str(sudoku.grid[5])[1:-1]};{str(sudoku.grid[6])[1:-1]};{str(sudoku.grid[7])[1:-1]};{str(sudoku.grid[8])[1:-1]}"""
            file.write(row+"\n")
        print("nyt repossa sudokut")
        print(self.find_all())

    def create(self, original_sudoku):
        originals = self.find_all()
        originals.append(original_sudoku)
        self._write(originals)
        return original_sudoku


sudoku_repository = SudokuRepository(SUDOKUS_FILE_PATH)
original_sudokus_repository = OriginalSudokuRepository(ORIGINALS_FILE_PATH)
