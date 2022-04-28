import os

from dynaconf import Dynaconf

# Uso da dynaconf é estar em conformidade com aplicações voltadas para Nuvem
# $ export BEERLOG_DATABASE__url="sqlite:///testing.db"
# Colocar no Jenkins (CI) o .env para o ambiente de test

settings = Dynaconf(
    envvar_prefix="BEERLOG",
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml"],
)
