# System import
from rich.table import Table

# Local import
from core.cli.cli import app
from core.utils.console import console
from core.database.controler import database_controler

@app.command()
def status() -> None:
    """
    Display logs and database infos.
    """
    display_banner()
    display_logs_count()
    display_top_ip()

def display_banner() -> None:
    console.print(f"[blue][*] Running status command...[/blue]")

def display_logs_count() -> None:
    database_controler.run_sql(
        """
            SELECT COUNT(*) FROM logs;        
        """
    )
    
    result = database_controler.fetchall()

    if (result):
        console.print(f"[*] Database contain [blue]{result[0][0]} entries [/blue]")
    else:
        console.print(f"[red][!] Unable to get entrie count[/red]")

def display_top_ip() -> None:
    database_controler.run_sql(
        """
            SELECT source_ip, COUNT(source_ip) AS 'value_occurence'
            FROM logs GROUP BY source_ip ORDER BY COUNT(source_ip) DESC
            LIMIT 5;
        """
    )

    result = database_controler.fetchall()
    
    if (result):
        console.print("[*] TOP source IP entries")
        table = Table()
        table.add_column("IP", style="yellow", justify="right")
        table.add_column("Count", style="cyan", justify="right")
        
        for entry in result:
            table.add_row(entry[0], str(entry[1]))
        console.print(table) 

    else:
        console.print(f"[red][!] Unable to get top IP count[/red]")
    

