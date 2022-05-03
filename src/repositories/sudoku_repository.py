# Tästä tulee repositoriot alkuperäisten sudokujen lisäämiselle ja muokatuille sudokuille

from pathlib import Path
from config import ORIGINALS_FILE_PATH, SUDOKUS_FILE_PATH
from entities.sudoku import OriginalSudoku, Sudoku


class OriginalSudokuRepository:
    """Alkuperäisten sudokun numeroihin liittyvästä pysyväistallennuksesta ja numeroiden
    etsimisestä vastaava luokka.
    """

    def __init__(self, file_path):
        """Konstruktori, joka luo uuden OriginalSudokuRepository -luokan olion.

        Args:
            file_path: Polku tiedostoon, johon alkuperäiset sudokun numerot on tallennettu.
        """
        self.file_path = file_path

    def ensure_file_exists(self):
        Path(self.file_path).touch()

    def find_all(self):
        """Palauttaa kaikki alkuperäiset sudokut.

        Returns:
            Lista alkuperäisistä sudokuista.
        """
        return self.read()

    def find_by_id(self, id_number):
        """Etsii alkuperäiset numerot annetun alkuperäisen sudokun id:n perusteella.

        Args:
            id_number: Käyttäjän käyttöliittymässä klikkaaman sudokun id

        Returns:
            OriginalSudoku -luokan olion, jolla on kyseinen id -numero.
        """
        sudokus = self.find_all()
        current_sudoku = filter(
            lambda sudoku: sudoku.id == id_number, sudokus
        )
        return list(current_sudoku)[0]

    def read(self):
        """Lukee csv -tiedostosta kaikki alkuperäiset sudokut.

        Returns:
            Listan alkuperäisistä sudokuista OriginalSudoku -olioina.
        """
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
                original_sudokus.append(
                    OriginalSudoku(id=sudoku_id, grid=grid))
        return original_sudokus

    def delete_all(self):
        """Poistaa kaikki alkuperäiset sudokut.
        """
        self._write([])

    def _write(self, originals):
        """Kirjoittaa csv -tiedostoon kaikki parametrina annetut alkuperäiset sudokut.

        Args:
            Lista alkuperäisistä sudokuista OriginalSudoku -olioina.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            for original_sudoku in originals:
                row = f"""{original_sudoku.id};{str(original_sudoku.grid[0])[1:-1]};{str(original_sudoku.grid[1])[1:-1]};{str(original_sudoku.grid[2])[1:-1]};{str(original_sudoku.grid[3])[1:-1]};{str(original_sudoku.grid[4])[1:-1]};{str(original_sudoku.grid[5])[1:-1]};{str(original_sudoku.grid[6])[1:-1]};{str(original_sudoku.grid[7])[1:-1]};{str(original_sudoku.grid[8])[1:-1]}"""
                file.write(row+"\n")

    def create(self, original_sudoku):
        """Kirjoittaa csv -tiedostoon uuden alkuperäisen sudokun tiedot.

        Args:
            original_sudoku: Lisättävä alkuperäinen sudoku OriginalSudoku -luokan oliona.

        Returns:
            Lisätyn sudokun OriginalSudoku -luokan oliona.
        """
        originals = self.find_all()
        originals.append(original_sudoku)
        self._write(originals)
        return original_sudoku


class SudokuRepository:
    """Käyttäjän sudoku -ratkaisuihin liittyvästä pysyväistallennuksesta huolehtiva luokka.
    """

    def __init__(self, file_path):
        """Konstruktori, joka luo uuden SudokuRepository -luokan olion.

        Args:
            file_path: Polku tiedostoon, johon käyttäjän lisäämät sudokun numerot on
            tallennettu/tallennetaan.
        """
        self.file_path = file_path

    def ensure_file_exists(self):
        Path(self.file_path).touch()

    def find_all(self):
        return self.read()

    def find_by_id_and_user(self, original_sudoku_id, user_name):
        """Etsii käyttäjän keskeneräisen ratkaisun alkuperäisen sudokun id:n ja käyttäjän nimen
        perusteella.

        Args:
            original_sudoku_id: Käyttäjän käyttöliittymässä klikkaaman alkuperäisen sudokun id
            user_name: Sisään kirjautuneen käyttäjän käyttäjänimi

        Returns:
            Käyttäjän keskeneräisen ratkaisun, jos sellainen löytyy.
            Tyhjän default -sudokun, jos käyttäjä ei ole vielä luonut ratkaisua kyseiseen sudokuun.
        """
        sudokus = self.find_all()
        self.original_sudoku_id = original_sudoku_id
        self.user_name = user_name
        current_sudoku = filter(self._filtering_function, sudokus)
        try:
            return list(current_sudoku)[0]
        except IndexError:
            return Sudoku(original_sudoku_id=self.original_sudoku_id)

    def _filtering_function(self, sudoku):
        """Find_by_id_and_user() -metodin käyttämä metodi oikean sudokun filtteröimiseen.

        Args:
            sudoku: csv -tiedostoon lisätty sudoku Sudoku -oliona, jonka attribuutteja
            verrataan etsittäviin attribuutteihin

        Returns:
            Totuusarvon, joka kertoo täyttääkö kyseinen sudoku filter -funktion ehdot.
        """
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
                sudokus.append(
                    Sudoku(original_sudoku_id=original_sudoku_id, grid=grid, user=user_name))
        return sudokus

    def delete_all(self):
        self._write([])

    def _write(self, sudokus):
        with open(self.file_path, "w", encoding="utf-8") as file:
            for sudoku in sudokus:
                row = f"""{sudoku.id};{str(sudoku.grid[0])[1:-1]};{str(sudoku.grid[1])[1:-1]};{str(sudoku.grid[2])[1:-1]};{str(sudoku.grid[3])[1:-1]};{str(sudoku.grid[4])[1:-1]};{str(sudoku.grid[5])[1:-1]};{str(sudoku.grid[6])[1:-1]};{str(sudoku.grid[7])[1:-1]};{str(sudoku.grid[8])[1:-1]}"""
                file.write(row+"\n")

    def delete_old_numbers(self, original_sudoku_id, user_name):
        """Poistaa csv -tiedostosta käyttäjän aiemmin luoman ratkaisun alkuperäisen sudokun
        id:n ja käyttäjänimen perusteella.

        Args:
            original_sudoku_id: Käyttäjän käyttöliittymässä klikkaaman alkuperäisen sudokun id
            user_name: Sisään kirjautuneen käyttäjän käyttäjänimi
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open(self.file_path, "w", encoding="utf-8") as file:
            for line in lines:
                if f"{original_sudoku_id};{user_name}" not in line.strip("\n"):
                    file.write(line)

    def write_new_numbers(self, sudoku):
        """Kirjoittaa uudet numerot csv -tiedoston loppuun

        Args: Sudoku -luokan olio, jonka numerot tulee kirjoittaa tiedostoon"""
        with open(self.file_path, "a", encoding="utf-8") as file:
            row = f"""{sudoku.original_sudoku_id};{str(sudoku.user)};{str(sudoku.grid[0])[1:-1]};{str(sudoku.grid[1])[1:-1]};{str(sudoku.grid[2])[1:-1]};{str(sudoku.grid[3])[1:-1]};{str(sudoku.grid[4])[1:-1]};{str(sudoku.grid[5])[1:-1]};{str(sudoku.grid[6])[1:-1]};{str(sudoku.grid[7])[1:-1]};{str(sudoku.grid[8])[1:-1]}"""
            file.write(row+"\n")

    def create(self, original_sudoku):
        originals = self.find_all()
        originals.append(original_sudoku)
        self._write(originals)
        return original_sudoku


sudoku_repository = SudokuRepository(SUDOKUS_FILE_PATH)
original_sudokus_repository = OriginalSudokuRepository(ORIGINALS_FILE_PATH)
