

import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

SUDOKUS_FILENAME = os.getenv('SUDOKUS_FILENAME') or 'sudokus.csv'
SUDOKUS_FILE_PATH = os.path.join(dirname, '..', 'data', SUDOKUS_FILENAME)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)

ORIGINALS_FILENAME = os.getenv('ORIGINALS_FILENAME') or 'originals.sudoku'
ORIGINALS_FILE_PATH = os.path.join(dirname, '..', 'data', ORIGINALS_FILENAME)
