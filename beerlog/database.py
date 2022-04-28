# Omitindo os Warnings do SQL Alchemy

import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar

from sqlmodel import Session, create_engine

from beerlog import models
from beerlog.config import settings

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


# Arquivo de DB criado através dessa engine
# Arquivo setting.toml para armazenar as configs
engine = create_engine(settings.database.url)

# Criando o DB
models.SQLModel.metadata.create_all(engine)
# Automatizar a criação da sessão com o DB


def get_session():
    return Session(engine)
