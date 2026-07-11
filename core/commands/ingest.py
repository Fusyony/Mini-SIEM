# Local import
from core.cli.cli import app
from core.utils.console import console
from core.ingest.ingest import Ingest

@app.command()
def ingest(type : str, logfile: str) -> None:

    ingest = Ingest()

    match type:
        case "nginx":
            ingest.import_nginx_logfile(logfile)
        case _:
            console.print(f"[red][!] Unkown type {type}, possible parameters are:[/red]")
            console.print(f"[red]\t - nginx[/red]")