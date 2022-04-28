# Realiza as mesmas coisas do que a models.py, porém
# ao expor a uma API, evita que o BD esteja exposto
# Permite também adaptar os tratamentos de erro a WEB.
from datetime import datetime

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


# Saida das cervejas
class BeerOut(BaseModel):
    # Dados que serão expostos a API
    # Podemos formatar conforme a necessidade, remover atributos tb
    id: int
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0  # Padrao 0
    date: datetime


class BeerIn(BaseModel):
    # Dados que serão expostos a API
    # Podemos formatar conforme a necessidade, remover atributos tb
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    # cls = classe
    @validator("flavor", "image", "cost")
    # Arroba é basicamente codigo que pode ser aplicado em cima de funções
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return v
