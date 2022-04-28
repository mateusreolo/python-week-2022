from typing import List

from fastapi import FastAPI

# Framework similar ao Flask, Django
from beerlog.core import get_beers_from_database
from beerlog.database import get_session

# Não realizar na prática, para não expor o modelo
# Deve-se realizar o serializer, novo arquivo
from beerlog.models import Beer
from beerlog.serializer import BeerIn, BeerOut

api = FastAPI(title="Beerlog")  # ASGI
# Ao criar uma API -> Documentar


# Utilizando o decorator
@api.get("/beers", response_model=List[BeerOut])
def list_beers():
    # Apresentando ao frontend todos os atributos em formato de lista
    beers = get_beers_from_database()
    # Retornar todos os itens
    return beers


@api.post("/beers", response_model=BeerOut)
# É possível criar métodos assincronos
# async def app_beer(beer_in:BeerIn):
def app_beer(beer_in: BeerIn):
    # Criando um dicionario
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        # Capturar o ID gerado: refresh
        session.refresh(beer)
    return beer
