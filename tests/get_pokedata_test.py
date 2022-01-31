import requests_mock

from fastapi_pokedex_api.configs.pokeapi_config import PokeapiSettings
from fastapi_pokedex_api.pokeapi_requests import get_pokedata
from tests.pikachu_data_test import PIKACHU_DATA

POKEAPI_IP = "https://pokeapi.co/api/v2/pokemon-species/"


def test_get_pokedata_not_legendary() -> None:
    """Testing the pokeapi get request for a non-legendary pokemon"""
    with requests_mock.Mocker() as m:
        m.get(f"{POKEAPI_IP}pikachu", text=PIKACHU_DATA)
        assert (
            get_pokedata(
                ip_settings=PokeapiSettings(POKEAPI_IP=POKEAPI_IP), poke_name="pikachu"
            ).is_legendary
            is False
        )


def test_get_pokedata_legenday() -> None:
    """Testing the pokeapi get request for a legendary pokemon"""
    assert (
        get_pokedata(
            ip_settings=PokeapiSettings(POKEAPI_IP=POKEAPI_IP), poke_name="mewtwo"
        ).is_legendary
        is True
    )


def test_get_pokedata_none_habitat() -> None:
    """Testing the pokeapi get request for a pokemon with None habitat"""
    assert (
        get_pokedata(
            ip_settings=PokeapiSettings(POKEAPI_IP=POKEAPI_IP), poke_name="piplup"
        ).habitat
        is None
    )
