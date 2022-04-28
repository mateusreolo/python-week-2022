from typing import Optional

import typer
from rich.console import Console

# Formatação do Texto -> Tabela
from rich.table import Table

from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Beer Management Application")

# Adapta os dados ao tamanho do Console
console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to Database")
    else:
        print("Couldn't add Beer to Database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lists beers in database."""
    beers = get_beers_from_database()
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        # Adicionar os dados as colunas
        # Automatizando a busca dos objetos baseados em Beer
        # beer.name, #beer.style
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
