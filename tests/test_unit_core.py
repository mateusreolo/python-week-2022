from beerlog.core import get_beers_from_database, add_beer_to_database


def test_add_beer_to_database():
    # Assert -> Assegure
    # Está enviando registros ao DB
    assert add_beer_to_database("Blue Moon", "Witbier", 10, 3, 6)


# Para teste unitário, um assert por funcao

# Após a configuração do conftest.py, as funções estão isoladas
# Por isso o add_beer teve que ser incluido nesta
def test_get_beers_from_database():
    # Arrange
    add_beer_to_database("Blue Moon", "Witbier", 10, 3, 6)
    # Act
    results = get_beers_from_database()
    # Assert
    assert len(results) > 0
