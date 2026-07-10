# System import
import sqlite3
import pathlib

# Local import
from core.utils.console import console

class Controler:
    
    def __init__ (self):
        self.db_name = "database.db"
        self.db_location = self.get_database_location()

        if not self.database_file_exist():
            console.print("[blue][*] No existing database found, creating new one... [/blue]")
            self.create_database()

        self.connection = self.create_connection()

    def create_database(self):
        open(self.db_location, "x").close()
        with sqlite3.connect(self.db_location) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_ip TEXT,
                    destination_ip TEXT,
                    user TEXT,
                    protocole TEXT,
                    status_code INTEGER,
                    timestamp DATETIME,
                    message TEXT,
                    log_type TEXT,
                    raw_log TEXT
                )
                """
            )
            connection.commit()
        console.print("[green][*] Database created successfully[/green]")

    def get_database_location(self) -> pathlib.Path:
        location = pathlib.Path(__file__).parent.parent.parent.resolve()
        location = location.joinpath(location, "database/database.db")
        return (location)

    def database_file_exist(self) -> bool:
        return (self.db_location.exists())

    def create_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_location)

    def insert_log(self, data: dict):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(
                """
                INSERT INTO logs (source_ip, destination_ip, user, protocole, status_code, timestamp, message, log_type, raw_log)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    data.get("source_ip"),
                    data.get("destination_ip"),
                    data.get("user"),
                    data.get("protocole"),
                    data.get("status_code"),
                    data.get("timestamp"),
                    data.get("message"),
                    data.get("log_type"),
                    data.get("raw_log")
                )
            )
            self.connection.commit()


database_controler = Controler()