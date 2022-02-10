import os

import fastapi
import pytest
import requests
import requests_mock

from fastapi_pokedex_api.configs.pokeapi_config import PokeapiSettings, get_pokeapi_ip
from fastapi_pokedex_api.pokeapi_requests import get_pokedata

POKEAPI_IP = "https://pokeapi.co/api/v2/pokemon-species/"


def test_get_pokedata_not_jsonable() -> None:
    """Testing the pokeapi get request for a non-legendary pokemon"""
    with requests_mock.Mocker() as m:
        m.get(f"{POKEAPI_IP}pikachu", text="not json")
        with pytest.raises(fastapi.HTTPException):
            get_pokedata(
                ip_settings=PokeapiSettings(POKEAPI_IP=POKEAPI_IP), poke_name="pikachu"
            )


def test_get_pokedata_invalid_json() -> None:
    with requests_mock.Mocker() as m:
        m.get(f"{POKEAPI_IP}pikachu", json={"not": "valid"})
        with pytest.raises(fastapi.HTTPException):
            get_pokedata(
                ip_settings=PokeapiSettings(POKEAPI_IP=POKEAPI_IP), poke_name="pikachu"
            )


def test_get_pokedata_bad_status_code() -> None:
    """Testing the pokeapi get request for a non-legendary pokemon"""
    with requests_mock.Mocker() as m:
        m.get(f"{POKEAPI_IP}pikachu", status_code=404)
        with pytest.raises(fastapi.HTTPException):
            get_pokedata(
                ip_settings=PokeapiSettings(POKEAPI_IP=POKEAPI_IP), poke_name="pikachu"
            )


def test_get_pokedata_failed_connection() -> None:
    with requests_mock.Mocker() as m:
        m.get(f"{POKEAPI_IP}pikachu", exc=requests.exceptions.ConnectionError)
        with pytest.raises(fastapi.HTTPException):
            get_pokedata(
                ip_settings=PokeapiSettings(POKEAPI_IP=POKEAPI_IP), poke_name="pikachu"
            )


def test_pokeapi_ip_envvar() -> None:
    os.environ["POKEAPI_IP"] = "https://pokeapi.co/api/v2/pokemon-species/"
    assert get_pokeapi_ip().POKEAPI_IP == "https://pokeapi.co/api/v2/pokemon-species/"
