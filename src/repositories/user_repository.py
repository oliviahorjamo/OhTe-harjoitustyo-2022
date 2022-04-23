from sqlite3 import Cursor
from database_connection import get_database_connection
from entities.user import User

def get_user_by_row(row):
    if row:
        return User(row["username"], row["password"])
    else:
        return None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username = ?",(username,))
        row = cursor.fetchone()
        return get_user_by_row(row)

    def create(self, user):
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?,?)", (user.username, user.password))
        self._connection.commit()
        return user

user_repository = UserRepository(get_database_connection())
users = user_repository.find_all()