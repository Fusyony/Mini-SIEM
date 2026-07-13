# System Import
import typer

help_message = """
--- Mini-SIEM --- \n
Simple tool to ingest and analyse logs.\n
Developped only to learning purpose.\n
-----------------\n
"""

# app instance (managing the cli)
app = typer.Typer(
    help=help_message
)

# Import all commands
import core.commands.ingest
import core.commands.status