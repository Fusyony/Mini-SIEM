# System Import
from typer import Option

# Local Import
from core.cli.cli import app
from core.utils.console import console
from core.ingest.ingest import Ingest

@app.command()
def ingest(
        logtype : str = Option(..., "--type", "-t", help="Type of logs to ingest."), 
        logfile: str = Option(..., "--file", "-f", help="Location of the file to ingest.")
    ) -> None:
    """
    Import a log file and insert it to the database.
    """

    ingest = Ingest()

    # [TODO]: Import available logtype throught the ingest class
    match logtype:
        case "nginx":
            ingest.import_nginx_logfile(logfile)
        case _:
            console.print(f"[red][!] Unkown type {type}, possible parameters are:[/red]")
            console.print(f"[red]\t - nginx[/red]")

