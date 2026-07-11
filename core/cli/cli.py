import typer

app = typer.Typer()

# Import all commands
import core.commands.ingest
import core.commands.status