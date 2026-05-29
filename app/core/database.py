import sqlite3
from pathlib import Path

DATABASE_NAME = "geekstore.db"


class Database:
    def __init__(self):
        self.db_path = Path(DATABASE_NAME)

    def connect(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection


class DatabaseInitializer:
    def __init__(self, database):
        self.database = database

    def initialize(self):
        connection = self.database.connect()

        connection.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                nome TEXT PRIMARY KEY,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL
            )
        """)

        total = connection.execute(
            "SELECT COUNT(*) FROM produtos"
        ).fetchone()[0]

        if total == 0:
            produtos = [
                ("teclado", 200.0, 10),
                ("mouse", 100.0, 5),
                ("monitor", 900.0, 3)
            ]

            connection.executemany(
                "INSERT INTO produtos VALUES (?, ?, ?)",
                produtos
            )

        connection.commit()
        connection.close()