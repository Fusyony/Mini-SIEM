from core.cli.cli import app
from core.utils.console import console

@app.command()
def ingest(type : str, logfile: str) -> None:

    match type:
        case "nginx":
            console.print(f"[blue][*] Importing nginx file {logfile}[/blue]")
        case _:
            console.print(f"[red][!] Unkown type {type}, possible parameters are:[/red]")
            console.print(f"[red]\t - nginx[/red]")

#TMP juste pour voir le bon r
@app.command()
def truc(type : str, logfile: str) -> None:

    match type:
        case "nginx":
            console.print(f"[blue][*] Importing nginx file {logfile}[/blue]")
        case _:
            console.print(f"[red][!] Unkown type {type}, possible parameters are:[/red]")
            console.print(f"[red]\t - nginx[/red]")