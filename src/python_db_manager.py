import sqlite3
from pathlib import Path

class OpenDatabase:
    def __init__(self):
        data_dir = Path(__file__).resolve().parent.parent / 'data'
        data_dir.mkdir(exist_ok=True)
        self.db_name = data_dir / 'pystock.db'
        self.connection = None
        self._cursor = None
        self.db_connect()
        self.db_create_table()
    

    def db_connect(self):
        self.connection = sqlite3.connect(str(self.db_name))
        self.connection.row_factory = sqlite3.Row
        self._cursor = self.connection.cursor()

    def db_create_table(self):
        self._cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER DEFAULT 0,
            price REAL NOT NULL
        );
        """)

    def db_insert_item(self, name, quantity, price):
        self._cursor.execute("""
        INSERT INTO stock (name, quantity, price) VALUES (?, ?, ?);
        """, (name, quantity, price))
        self.db_commit()

    def db_commit(self):
        self.connection.commit()

    def db_close(self):
        self.connection.close()

    def db_fetch_all(self):
        self._cursor.execute("SELECT * FROM stock;")
        return self._cursor.fetchall()

    def db_search_item(self, search_term):
        self._cursor.execute("SELECT * FROM stock WHERE name LIKE ? OR id = ?;", (f"%{search_term}%", search_term))
        return self._cursor.fetchall()

    def db_remove_item(self, item_name):
        self._cursor.execute("DELETE FROM stock WHERE name = ?;", (item_name,))
        self.db_commit()

    def db_update_item(self, id, new_name, new_quantity, new_price):
        self._cursor.execute("""
        UPDATE stock 
        SET name = ?, quantity = ?, price = ?
        WHERE id = ?;
        """, (new_name, new_quantity, new_price, id))
        self.db_commit()