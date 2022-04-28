# from dataclasses import dataclass
from datetime import datetime

# Classificar os ratings
from statistics import mean
from typing import Optional

# Para validar o conteudo recebido
from pydantic import validator
from sqlmodel import Field, SQLModel

# Decorator
# @dataclass
# class Beer:
#    #validação dos dados que estão chegando
#    name: str
#    style:str
#    flavor:int
#    image:str
#    cost:int


class Beer(SQLModel, table=True):
    # Notação opcional do id passado pelo usuário, o sistema deve controlar os ids
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0  # Padrao 0
    date: datetime = Field(default_factory=datetime.now)

    # cls = classe
    @validator("flavor", "image", "cost")
    # Arroba é basicamente codigo que pode ser aplicado em cima de funções
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    # Always = True, sempre calcula media após o input
    # Em values, estamos trazendo o que o pydantic trata para values
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


# brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6,image=8,cost=8)

# try:
#    brewdog = Beer(name="Brewdog", style="NEIPA", flavor=60,image=8,cost=8)
# except RuntimeError:
#    print("Aqui deu erro")
