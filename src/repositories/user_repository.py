from database_connection import get_database_connection
from entities.user import User


def get_user_by_row(row):
    if row:
        return User(row["username"], row["password"])
    return None


class UserRepository:
    """Käyttäjien tietoja hallitseva luokka.
    """

    def __init__(self, connection):
        """Konstruktori, joka luo uuden UserRepository -olion.

        Args:
            connection: tietokantaan luotu yhteys Connection -oliona
        """
        self._connection = connection

    def find_all(self):
        """Etsii kaikki käyttäjät.

        Returns:
            Lista User -olioita
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def find_by_username(self, username):
        """Etsii käyttäjän kyseisellä käyttäjänimellä

        Args:
            username: Käyttäjän käyttöliittymässä antama käyttäjänimi

        Returns:
            Kyseisen käyttäjän User -oliona.
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username = ?", (username,))
        row = cursor.fetchone()
        return get_user_by_row(row)

    def create(self, user):
        """Lisää uuden käyttäjän tietokantaan.

        Args:
            user: User -luokan -olio, joka luotu käyttäjän antaman käyttäjänimen ja salasanan
            avulla.

        Returns:
            Tallennettu käyttäjä User -luokan oliona.
        """
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?,?)",
                       (user.username, user.password))
        self._connection.commit()
        return user

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
users = user_repository.find_all()
