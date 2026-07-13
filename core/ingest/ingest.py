# System imports
from os import path
import time

# Local imports
from core.utils.console import console
from core.database.controler import database_controler

class Ingest():
    
    def import_nginx_logfile(self, filepath: str) -> bool:
        from core.normalizer.nginx_normalizer import NginxNormalizer
        
        line_count = 0
        normalizer = NginxNormalizer()

        # Return is file don't exist
        if (not path.isfile(filepath)):
            console.print(f"[red][!] File {filepath} does not exist[/red]")
            return (False)

        fd = open(filepath, "r")

        # Return if file is not readable
        if (not fd.readable()):
            console.print(f"[red][!] File {filepath} is not readable[/red]")
            return (False)

        console.print(f"[blue][*] Importing logs from nginx log file {filepath}[/blue]")

        for line in fd:
            normalized_log = normalizer.normalize_log(line)
            if (normalized_log != {}):
                normalized_log["raw_log"] = line.strip()
                normalized_log["log_type"] = "nginx"
                # Insert log don't commit to the database.
                self.insert_log(normalized_log)
                line_count += 1

        # Commit the changes to the database (only once at the end to improve performance)
        database_controler.commit()

        console.print(f"[green][*] {line_count} log entries imported from {filepath}[/green]")
        return (True)

    def insert_log(self, data : dict) -> None:
        database_controler.run_sql(
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