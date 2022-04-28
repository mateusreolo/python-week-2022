import pytest
from unittest.mock import patch
from sqlmodel import create_engine
from beerlog import models

#Arquivo com Mock

#Para cada função no arquivo de testes
#Cria um novo diretório
#Cria um novo db
#Conecta a engine com o novo db
@pytest.fixture(autouse=True, scope="function")
def each_test_uses_separate_database(request):
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = tmpdir.join("beerlog.test.db")
    engine = create_engine(f"sqlite:///{test_db}")
    models.SQLModel.metadata.create_all(bind=engine)
    #Faz a substituição do engine
    with patch("beerlog.database.engine", engine):
        #yield: return do protocolo generator, para gerar dados/informações
        yield