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
            console.print("[blue][*] Creation of the database[/blue]")
            self.create_database()

        self.connection = self.create_connection()

    def create_database(self):
        open(self.db_location, "x").close()

    def get_database_location(self) -> pathlib.Path:
        location = pathlib.Path(__file__).parent.parent.parent.resolve()
        location = location.joinpath(location, "database/database.db")
        return (location)

    def database_file_exist(self) -> bool:
        return (self.db_location.exists())

    def create_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_location)
