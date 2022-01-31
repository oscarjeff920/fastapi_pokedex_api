from fastapi_pokedex_api.pokeapi_requests import get_pokedata
from fastapi_pokedex_api.pokedex_schema import PokedexBase


# def test_get_pokedata_not_legendary() -> None:
#     """Testing the pokeapi get request for a non-legendary pokemon"""
#     assert get_pokedata(poke_name="pikachu").is_legendary is True
#
#
# def test_get_pokedata_legenday() -> None:
#     """Testing the pokeapi get request for a legendary pokemon"""
#     assert get_pokedata(poke_name="mewtwo").is_legendary is False
#
#
# def test_get_pokedata_none_habitat() -> None:
#     """Testing the pokeapi get request for a pokemon with None habitat"""
#     assert get_pokedata(poke_name="piplup").habitat is None
