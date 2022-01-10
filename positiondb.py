import sqlite3
from typing import Tuple


class PositionDB:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('position.db')

    def close(self) -> None:
        self.conn.close()

    def drop_table(self):
        sql = "DROP TABLE IF EXISTS position;"
        cur = self.conn.cursor()
        cur.execute(sql)

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS position (
                ID integer PRIMARY KEY AUTOINCREMENT,
                name string NOT NULL,
                lat float NOT NULL,
                lon float NOT NULL
            );"""
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def insert_location(self, address: str, lat:float, lon:float) -> None:
        sql = "INSERT INTO position (name,lat,lon) VALUES (?,?,?)"
        cur = self.conn.cursor()
        cur.execute(sql, (address, lat, lon))
        self.conn.commit()

    def get_location(self, address:str) -> Tuple[int, int]:
        sql = "SELECT lat, lon FROM position WHERE name = :address"
        cur = self.conn.cursor()
        cur.execute(sql, {'address': address})
        try:
            rows = cur.fetchone()
            return rows[0], rows[1]
        except:
            return None, None

    def print_all_location(self) -> None:
        sql = "SELECT name, lat, lon FROM position"
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
