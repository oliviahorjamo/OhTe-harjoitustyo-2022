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
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self):
        """Luokan konstruktori, joka luo uuden sovelluslogiikasta vastaavan olion."""
        self._user = None
        self._user_repository = user_repository
        self.original_sudokus_repository = original_sudokus_repository
        self.sudoku_repository = sudoku_repository

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: käyttäjän antama uniikki käyttäjänimi
            password: käyttäjän antama vähintään 1 merkkiä pitkä käyttäjänimi
        Raises:
            InvalidCredentialsError: Virhe, joka tapahtuu, jos käyttäjätunnus ja salasana
            eivät täsmää tai jos käyttäjää ei löydy.
        Returns:
            user: Kirjautuneen käyttäjän tiedoilla luotu User-olio
        """

        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError('Invalid username or password')
        self._user = user
        return user

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja mahdollisesti kirjaa tämän sisään.

        Args:
            username: Väh. 1 merkkiä pitkä merkkijono, joka kuvaa käyttäjän käyttäjänimeä.
            password: Väh. 1 merkkiä pitkä merkkijono, joka kuvaa käyttäjän antamaa salasanaa.
            login (bool, optional): Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään
            onnistuneen käyttäjän luonnin jälkeen.

        Raises:
            UsernameExistsError: Virhe, joka annetaan, jos käyttäjänimellä löytyy jo käyttäjä.

        Returns:
            user: Käyttäjän tiedoilla luotu User -olio.
        """
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user

    def find_original_numbers(self, original_numbers_id):
        """Etsii kyseisellä id -numerolla olevan sudokun alkuperäiset numerot.

        Args:
            original_numbers_id: Käyttäjän klikkaaman sudokun id -numero.

        Returns:
            Kyseisellä id -numerolla ja sillä löytyvillä alkuperäisillä numeroilla
            luotu OriginalSudoku -luokan olio.
        """
        return self.original_sudokus_repository.find_by_id(original_numbers_id)

    def find_added_numbers(self, original_numbers_id):
        """Etsii käyttäjän id:n ja alkuperäisen sudokun id:n avulla käyttäjän lisäämät numerot

        Args:
            original_numbers_id: Käyttäjän klikkaaman sudokun id -numero.

        Returns:
            Kyseisillä id -numeroilla löytynyt käyttäjän aiemmin tallentama sudokun ratkaisu
            tai tyhjä sudoku, jos käyttäjä ei ole lisännyt vielä yhtäkään numeroa."""
        return self.sudoku_repository.find_by_id_and_user(original_numbers_id, self._user.username)

    def add_number(self, originals, sudoku, row, column, number):
        """Lisää käyttäjän käyttöliittymässä antaman numeron Sudoku -olion grid -attributtiin.
        Poistaa käyttäjän aiemmin tähän sudokuun luoman ratkaisun csv -tiedostosta ja kirjoittaa
        tilalle nykyisen ratkaisun.

        Args:
            originals: kyseisen sudokun alkuperäiset numerot listana
            sudoku: nykyinen muokattava sudoku Sudoku -oliona
            row: rivi, johon uusi numero tulisi lisätä
            column: sarake, johon uusi numero tulisi lisätä
            number: käyttäjän lisäämä numero

        Returns:
            Totuusarvo, joka kertoo onnistuiko numeron lisääminen.
        """
        if self.test_square_empty(originals, sudoku, row, column):
            sudoku.grid[row][column] = number
            self.sudoku_repository.delete_old_numbers(original_sudoku_id=sudoku.original_sudoku_id,
                                                      user_name=self._user.username)
            self.sudoku_repository.write_new_numbers(sudoku)
            return True
        return False

    def delete_number(self, originals, sudoku, row, column):
        """Poistaa käyttäjän lisäämän numeron. Poistaa käyttäjän aiemmin tähän sudokuun
        luoman ratkaisun csv-tiedostosta ja kirjoittaa tilalle nykyisen ratkaisun.

        Args:
            originals: kyseisen sudokun alkuperäiset numerot listana
            sudoku: nykyinen muokattava sudoku Sudoku -oliona
            row: rivi, josta käyttäjä haluaa poistaa numeron
            column: sarake, josta käyttäjä haluaa poistaa numeron

        Returns:
            Totuusarvo, joka kertoo onnistuiko numeron poistaminen.
        """
        if self.test_can_delete(originals, row, column):
            sudoku.grid[row][column] = 0
            self.sudoku_repository.delete_old_numbers(original_sudoku_id=sudoku.original_sudoku_id,
                                                      user_name=self._user.username)
            self.sudoku_repository.write_new_numbers(sudoku)
            return True
        return False

    def test_square_empty(self, originals, sudoku, row, column):
        """Tarkistaa, onko ruutu tyhjä eli ei sisällä käyttäjän lisäämää numeroa tai alkuperäistä
        numeroa.

        Args:
            originals: kyseisen sudokun alkuperäiset numerot listana
            sudoku: nykyinen muokattava sudoku Sudoku -oliona
            row: rivi, johon uusi numero tulisi lisätä
            column: sarake, johon uusi numero tulisi lisätä

        Returns:
            Totuusarvo, joka kertoo, onko kyseinen ruutu tyhjä.
        """
        if sudoku.grid[row][column] == 0 and originals[row][column] == 0:
            return True
        return False

    def test_can_delete(self, originals, row, column):
        """Tarkistaa, sisältääkö valittu ruutu alkuperäisen numeron.

        Args:
            originals: kyseisen sudokun alkuperäiset numerot listana
            row: rivi, josta numero halutaan poistaa
            column: sarake, josta numero halutaan poistaa

        Returns:
            Totuusarvo, joka kertoo, sisältääkö ruutu alkuperäisen numeron.
        """
        if originals[row][column] == 0:
            return True
        return False

    def find_all_sudokus(self):
        """Etsii kaikki sovelluksesta löytyvät valmiit sudokut.

        Returns:
            Lista, jossa kaikki alkuperäiset sudokut OriginalSudoku -olioina.
        """
        return self.original_sudokus_repository.find_all()


sudoku_service = SudokuService()
