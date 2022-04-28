# Testes para o CLI do Beerlog
from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()

# Para testes funcionais, pode-se utilizar mais de um assert
def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )
    # Retorno sucesso do terminal unix
    assert result.exit_code == 0
    assert "Beer added" in result.stdout
