from typing import List

from sqlmodel import select

from beerlog.database import get_session
from beerlog.models import Beer


def add_beer_to_database(
    name: str, style: str, flavor: int, image: int, cost: int
) -> bool:  # Essa notação indica o que a função retorna

    with get_session() as session:
        beer = Beer(
            name=name,
            # name=name.lower(), ##Ao salvar o valor, str convertida pra lower()
            style=style,
            flavor=flavor,
            image=image,
            cost=cost,
        )
        session.add(beer)  # INSERT INTO beer VALUES [...]
        session.commit()
    return True


def get_beers_from_database() -> List[
    Beer
]:  # Cada objeto na lista é um objeto Beer
    with get_session() as session:
        sql = select(Beer)  # SELECT * FROM BEER
        return list(session.exec(sql))  # List ocupa mais memória
